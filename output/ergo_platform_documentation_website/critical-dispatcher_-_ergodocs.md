# critical-dispatcher - ErgoDocs
Source: [https://docs.ergoplatform.com/node/conf/conf-crit/](https://docs.ergoplatform.com/node/conf/conf-crit/)
Generated: 2025-05-11

## Summary
The critical-dispatcher is a dedicated actor dispatcher, utilized exclusively by the block candidate generator and NodeViewHolder actors within the system. This dispatcher is integral to maintaining critical tasks which require isolation from other non-critical activities. type = Dispatcher This configuration sets the type of the dispatcher. In this case, it is set as Dispatcher.

## Keywords
dispatcher, actor, block, candidate, generator, system, task, isolation, activity, type, configuration, case, executor, thread, pool, mechanism, worker, size, number, throughput

## Content
## Critical-Dispatcher Configuration Settings#
The critical-dispatcher is a dedicated actor dispatcher, utilized exclusively by the block candidate generator and NodeViewHolder actors within the system. This dispatcher is integral to maintaining critical tasks which require isolation from other non-critical activities.

### Dispatcher Type#
type = Dispatcher

This configuration sets the type of the dispatcher. In this case, it is set as Dispatcher.

### Executor#
executor = "thread-pool-executor"

The executor is the mechanism responsible for running tasks given to it by the dispatcher. Here, it is configured to use the "thread-pool-executor", which creates a pool of worker threads for executing tasks.

#### fixed-pool-size#
fixed-pool-size = 2

This configuration specifies the number of threads in the thread pool for the thread-pool-executor. It is set to a fixed size of 2 in this configuration.

### Throughput#
throughput = 1

throughput is the maximum number of messages to be processed per actor before the thread is made available to other actors. This setting helps control how long a thread can be occupied by an actor. In this case, it is set to 1.

### Complete Configuration Code#
critical-dispatcher {
  type = Dispatcher
  executor = "thread-pool-executor"
  thread-pool-executor {
    fixed-pool-size = 2
  }
  throughput = 1
}

This configuration ensures that critical tasks handled by the block candidate generator and NodeViewHolder actors are allocated dedicated threads, thereby promoting efficient execution.
