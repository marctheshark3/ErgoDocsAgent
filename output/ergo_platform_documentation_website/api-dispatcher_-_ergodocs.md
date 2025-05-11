# api-dispatcher - ErgoDocs
Source: [https://docs.ergoplatform.com/node/conf/conf-api/](https://docs.ergoplatform.com/node/conf/conf-api/)
Generated: 2025-05-11

## Summary
The api-dispatcher configuration controls the dispatcher responsible for managing API-related actors. In actor-based systems, the dispatcher is responsible for the execution of messages from the actor's mailbox. type = Dispatcher

The type setting specifies the dispatcher type. In this configuration, Dispatcher is used, representing an event-based dispatcher. executor = "fork-join-executor"

The executor setting determines the type of execution service used.

## Keywords
dispatcher, configuration, actor, system, execution, message, mailbox, type, specifie, event, executor, fork, join, service, task, part, efficiency, parallelism, setting, number

## Content
## API Dispatcher Configuration#
The api-dispatcher configuration controls the dispatcher responsible for managing API-related actors. In actor-based systems, the dispatcher is responsible for the execution of messages from the actor's mailbox.

### Dispatcher Type#
type = Dispatcher

The type setting specifies the dispatcher type. In this configuration, Dispatcher is used, representing an event-based dispatcher.

### Executor Type#
executor = "fork-join-executor"

The executor setting determines the type of execution service used. Here, the fork-join-executor is utilized, which allows tasks to be split into smaller parts and executed concurrently, increasing efficiency.

#### Minimum Parallelism#
parallelism-min = 1

The parallelism-min setting indicates the minimum number of threads to cap the factor-based parallelism number.

#### Parallelism Factor#
parallelism-factor = 2.0

The parallelism-factor setting is used to calculate the parallelism, i.e., the number of threads. It is calculated as the ceiling of the number of available processors multiplied by the factor.

#### Maximum Parallelism#
parallelism-max = 2

The parallelism-max setting determines the maximum number of threads to cap the factor-based parallelism number.

### Throughput#
throughput = 4

The throughput setting defines the maximum number of messages processed per actor before the thread switches to the next actor. A lower value results in fairer, but potentially less efficient execution. Here, it's set to 4.

### Full Code Snippet#
api-dispatcher {
  type = Dispatcher
  executor = "fork-join-executor"
  fork-join-executor {
    parallelism-min = 1
    parallelism-factor = 2.0
    parallelism-max = 2
  }
  throughput = 4
}
Overall, the api-dispatcher configuration plays a crucial role in controlling the efficiency and fairness of processing messages for API-related actors in your application.
