import os
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import Schema


class ParquetSplitter:

    def __init__(self,
                 src_parquet_path: str,
                 target_dir: str,
                 num_chunks: int = 25
                 ):
        self._src_parquet_path = src_parquet_path
        self._target_dir = target_dir
        self._num_chunks = num_chunks

        self._src_parquet = pq.ParquetFile(
            self._src_parquet_path,
            memory_map=True,
        )

        self._total_group_num = self._src_parquet.num_row_groups
        self._schema = self._src_parquet.schema

    @property
    def num_row_groups(self):
        print(f'Total num of groups found: {self._total_group_num}')
        return self._src_parquet.num_row_groups

    @property
    def schema(self):
        return self._schema

    def read_rows(self):
        for elem in self._src_parquet.iter_batches(
                columns=['player_id', 'played_at']):
            elem: pa.RecordBatch
            print(elem.to_pydict())

    def split(self):
        for chunk_num, chunk_range in self._next_chunk_range():
            table = self._src_parquet.read_row_groups(row_groups=chunk_range)
            file_name = f'chunk_{chunk_num}.parquet'
            path = os.path.join(self._target_dir, file_name)
            print(f'Writing chunk #{chunk_num}...')
            pq.write_table(
                table=table,
                where=path,
            )

    def _next_chunk_range(self):
        upper_bound = self.num_row_groups
        
        chunk_size = upper_bound // self._num_chunks

        chunk_num = 0
        low, high = 0, chunk_size
        while low < upper_bound:
            group_range = list(range(low, high))
            
            yield chunk_num, group_range
            chunk_num += 1
            low, high = low + chunk_size, high + chunk_size
            if high > upper_bound:
                high = upper_bound

    @staticmethod
    def _get_row_hour(row: pa.RecordBatch):
        return row.to_pydict()['played_at'][0].hour


if __name__ == '__main__':
    splitter = BngParquetSplitter(
        src_parquet_path="path/to/Parquet",
        target_dir="path/to/result/dir",
        num_chunks=100,
    )
    splitter.split()