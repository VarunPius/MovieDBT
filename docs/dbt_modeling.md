# Intro
Data is usually a chaotic asset within an organisation, therefore it is always important to enforce structure whereas possible. 

# Staging, Intermediate and Mart models
Data models vary — and by this I mean that some data models may correspond to some specific data sources, others may combine together multiple sources or even other data models and so on. Therefore, it is important to create layers of data models. The proposed layering consists of three types of models namely staging models, intermediate models and mart models.

**Staging models**, are the building blocks of all data models in your dbt project. Staging models are supposed to include basic computations (such as bytes to gigabytes), renaming, type casting and categorisation (using `CASE WHEN` statements). However, you should **avoid performing any joins** and aggregations over staging model. And as a general rule of thumb, you should be having a 1–1 mapping between your data sources and staging models. Since staging models are not supposed to represent final artifacts, it is also recommended to materialize them as views.

**Intermediate models**, are supposed to bring together staging models or even other intermediate models and they tend to be a bit more complex than the staging ones. In other words, these models represent more meaningful building blocks that bring together information from multiple models. Note though that they aren’t supposed to be exposed to end users (i.e consumed by BI tools such as Tableau, PowerBI or Looker). Also it’s important to mention that — as a rule of thumb — if an intermediate model gets referenced in several places then you may have to consider building a macro instead, or perhaps re-consider the way you’ve designed your models.

**Mart models**, are business-defined entities that are supposed to be consumed by end users and business intelligence tools. Every mart model is meant to represent a fine-grained entity — payments, customers, users, orders are just a few examples of what we would represent as marts.
Structuring your dbt models

Now that we have a solid understanding about the three main model types in the context of data build too, let’s initiation the discussion with respect to how these models need to be structured in a meaningful way that will help data teams maintain and expand them in an easy and intuitive way.

Within your dbt project, you need to have a parent directory called models consisting of three directories, each of which representing one of the model types we discussed earlier:
```
models
|---intermediate
|---marts
|---staging
```

Now let’s start with staging models.
- For every distinct source, you need to create a subdirectory under `staging` directory
- Every model, must follow the `stg_[source]__[entity]s.sql` notation
- A `base` sub-directory under the model’s directory, in case you need to join together staging models

As an example, let’s suppose that we have three separate sources — one is Facebook Ads (marketing events), another one from Stripe (payments) and a third one containing business entities for -say- our online shop.
```
models/staging
|---facebook_ads
|   |---_facebook_ads__models.yml
|   |---_facebook_ads__sources.yml
|   |---_facebook_ads__events.yml
|---my_shop
|   |---_my_shop__models.yml
|   |---_my_shop__sources.yml
|   |---base
|   |  |---base_my_shop__deleted_products.sql
|   |  |---base_my_shop__deleted_users.sql
|   |  |---base_my_shop__products.sql
|   |  |---base_my_shop__users.sql
|   |---stg_my_shop__orders.sql
|   |---stg_my_shop__products.sql
|   |---stg_my_shop__users.sql
|---stripe
    |---_stripe_models.yml
    |---_stripe_models.yml
    |---stg_stripe__payments.yml
```

Notice how we creae a separete sub-directory for every distinct source, each of which consists of two yml files — one for defining the models and another one for sources — and as many staging models you have for each of the source.

Now let’s move on to intermediate models.
- For every distinct business group, we create a sub-directory — much like the staging structure we introduced earlier
- Every intermediate model, must follow the `int_[entity]s_[verb]s.sql` naming convention. Note that using verbs as part of the naming will help you build names which helps readers and maintainers cleary undersdtand what a particular model is supposed to do. Such verbs would be joined, aggregated, summed etc.

As an example, let’s suppose that we have two business groups, namely finance and marketing:
```
models/intermediate
|---finance
|   |---_int_finance__models.yml
|   |---int_payments_pivoted_to_orders.sql
|---marketing
|   |---_int_marketing__models.yml
|   |---int_events_aggregated_per_user_platform.sql
```

And finally, let’s see how we would struture our final building blocks, the mart models that correspond to business-defined entities.
- Create one sub-directory for every department, business unit or entity
- Every `mart` model, should simply be named after the entity it represents. For example, orders, users or payments
- Avoid duplicate entities across multiple different business units (this is usually an anti-pattern).
```
models/marts
|---finance
|   |---_finance__models.yml
|   |---orders.sql
|   |---payments.sql
|   |---payroll.sql
|   |---revenue.sql
|---marketing
|   |---_marketing__models.yml
|   |---campaigns.sql
|   |---users.sql
```

# Naming conventions: A recap
This was a fairly long article with too much information — especially if you are new to dbt — so let me recap some key points with respect to naming conventions.
- Under the `models` directory, create three sub-directories for each data model type
- Staging models need to follow the `stg_[source]__[entity]s.sql` naming convention
- Intermediate models need to follow the `int_[entity]s_[verb]s.sql` convention
- Mart models need to be named after the entity they represent
- A `base` sub-directory under the staging model’s directory, in case you need to join together staging models

# Final output
And here’s the final structure of the example we went through in the previous sections.
```
models
|---intermediate
   |---finance
   |   |---_int_finance__models.yml
   |   |---int_payments_pivoted_to_orders.sql
   |---marketing
   |   |---_int_marketing__models.yml
   |   |---int_events_aggregated_per_user_platform.sql
|---marts
    |---finance
    |   |---_finance__models.yml
    |   |---orders.sql
    |   |---payments.sql
    |   |---payroll.sql
    |   |---revenue.sql
    |---marketing
    |   |---_marketing__models.yml
    |   |---campaigns.sql
    |   |---users.sql
|---staging
   |---facebook_ads
   |   |---_facebook_ads__models.yml
   |   |---_facebook_ads__sources.yml
   |   |---_facebook_ads__events.yml
   |---my_shop
   |   |---_my_shop__models.yml
   |   |---_my_shop__sources.yml
   |   |---base
   |   |  |---base_my_shop__deleted_products.sql
   |   |  |---base_my_shop__deleted_users.sql
   |   |  |---base_my_shop__products.sql
   |   |  |---base_my_shop__users.sql
   |   |---stg_my_shop__orders.sql
   |   |---stg_my_shop__products.sql
   |   |---stg_my_shop__users.sql
   |---stripe
       |---_stripe_models.yml
       |---_stripe_models.yml
       |---stg_stripe__payments.yml
```

Obviously, the structure we demonstrated today may not be a 100% fit to your use-case so feel free to amend it accordingly — but whatever the case make sure to clearly define the logic behind this structuring and stick to it.
