


# [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")  — Thread-based parallelism[¶](https://docs.python.org/3/library/threading.html#module-threading "Permalink to this headline")
Python offers two built-in libraries for parallelization: multiprocessing and threading.
A Thread or a Thread of Execution is defined in computer science as the smallest unit that can be scheduled in an operating system. Threads are normally created by a fork of a computer script or program in two or more parallel (which is implemented on a single processor by multitasking) tasks. Threads are usually contained in processes. More than one thread can exist within the same process. These threads share the memory and the state of the process. In other words: They share the code or instructions and the values of its variables.  
  
There are two different kind of threads:

-   Kernel threads
-   User-space Threads or user threads

Kernel Threads are part of the operating system, while User-space threads are not implemented in the kernel.  
  
In a certain way, user-space threads can be seen as an extension of the function concept of a programming language. So a thread user-space thread is similar to a function or procedure call. But there are differences to regular functions, especially the return behaviour.

Every process has at least one thread, i.e. the process itself. A process can start multiple threads. The operating system executes these threads like parallel "processes". On a single processor machine, this parallelism is achieved by thread scheduling or timeslicing.

**Advantages of Threading:**

-   Multithreaded programs can run faster on computer systems with multiple CPUs, because theses threads can be executed truly concurrent.
-   A program can remain responsive to input. This is true both on single and on multiple CPU
-   Threads of a process can share the memory of global variables. If a global variable is changed in one thread, this change is valid for all threads. A thread can have local variables.

 **Disadvantages:**
    
   -  Kernel threads are generally slower to create and manage than the user threads.
    
    - Transfer of control from one thread to another within same process requires a mode switch to the Kernel.

Please note: The thread module has been considered as "deprecated" for quite a long time. Users have been encouraged to use the threading module instead. So,in Python 3 the module "thread" is not available anymore. But that's not really true: It has been renamed to "_thread" for backwards incompatibilities in Python3.  
  
The module "thread" treats a thread as a function, while the module "threading" is implemented in an object oriented way, i.e. every thread corresponds to an object.

In a specific implementation, the user threads must be mapped to kernel threads, using one of the following strategies.

#### Many-To-One Model

-   In the many-to-one model, many user-level threads are all mapped onto a single kernel thread.
-   Thread management is handled by the thread library in user space, which is very efficient.
-   However, if a blocking system call is made, then the entire process blocks, even if the other user threads would otherwise be able to continue.
-   Because a single kernel thread can operate only on a single CPU, the many-to-one model does not allow individual processes to be split across multiple CPUs.
- 
#### One-To-One Model

-   The one-to-one model creates a separate kernel thread to handle each user thread.
-   One-to-one model overcomes the problems listed above involving blocking system calls and the splitting of processes across multiple CPUs.
-   However the overhead of managing the one-to-one model is more significant, involving more overhead and slowing down the system.

#### Many-To-Many Model

-   The many-to-many model multiplexes any number of user threads onto an equal or smaller number of kernel threads, combining the best features of the one-to-one and many-to-one models.
-   Users have no restrictions on the number of threads created.
-   Blocking kernel system calls do not block the entire process.
-   Processes can be split across multiple processors.
-   Individual processes may be allocated variable numbers of kernel threads, depending on the number of CPUs present and other factors.

## Global Interpreter Lock

### What is GIL ?

Wiki Definition: Global interpreter lock (GIL) is a mechanism used in computer language interpreters to synchronize the execution of threads so that only one native thread can execute at a time.

### Why python uses GIL ?

In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe.

> **Thread safety**: A piece of code is thread-safe if it functions correctly during simultaneous execution by multiple threads.

**Benefits of the GIL**

-   Easy integration of C libraries that usually are not thread-safe.
-   It is faster in the single-threaded case.
-   It is faster in the multi-threaded case for i/o bound programs.
-   It is faster in the multi-threaded case for cpu-bound programs that do their compute-intensive work in C libraries.

### What is the problem if it exists ?

The GIL does not prevent threading. All the GIL does is make sure only one thread is executing Python code at a time; control still switches between threads. Hence, It prevents multithreaded CPython programs from taking full advantage of multiprocessor systems in certain situations.

Note that potentially blocking or long-running operations, such as I/O, image processing, and NumPy number crunching, happen outside the GIL. Therefore it is only in multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL becomes a bottleneck.

### Solutions to overcome the problem ?

-   The GIL is a problem if, and only if, you are doing CPU-intensive work in pure Python.
-   What many server deployments then do, is run more than one Python process, to let the OS handle the scheduling between processes to utilize your CPU cores to the max. You can also use the multiprocessing library to handle parallel processing across multiple processes from one codebase and parent process, if that suits your use cases.
-   The GIL can be released by C extensions.
-   Python’s standard library releases the GIL around each blocking i/o call. Thus the GIL has no consequence for performance of i/o bound servers. You can thus create networking servers in Python using processes (fork), threads or asynchronous i/o, and the GIL will not get in your way.
-   There are several implementations of Python, for example, CPython, IronPython, RPython, etc.Some of them have a GIL, some don’t. For example, CPython has the GIL.
-   Python threading is great for creating a responsive GUI, or for handling multiple short web requests where I/O is the bottleneck more than the Python code. It is not suitable for parallelizing computationally intensive Python code, stick to the multiprocessing module for such tasks.

> Threads are usually a bad way to write most server programs. If the load is low, forking is easier. If the load is high, asynchronous i/o and event-driven programming (e.g. using Python’s Twisted framework) is better. The only excuse for using threads is the lack of os.fork on Windows.

A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other codes. For simplicity, you can assume that a thread is simply a subset of a process!

  

## **Locks**

These are the simplest primitive for synchronization in Python. There are two states of a lock i.e **locked and unlocked**. A lock is a class in the threading module whose object generated in the unlocked state and has two primary methods i.e `acquire()` and `release()`. When the acquire() method is called, it locks the execution of the Lock and blocks its execution until the release() method is called in some other thread which sets it to unlock state. Locks help us in efficiently accessing a shared resource in a program in order to prevent corruption of data, it follows mutual exclusion as only one thread can access a particular resource at a time.

## **RLocks**

The default Lock doesn't recognize which thread the lock currently holds. If the shared resource is being accessed by any thread then other threads trying to access the shared resource will get blocked even if it is the same thread that locked the shared resource. The Re-entrant lock or RLock is used in these situations to prevent undesired blocking from accessing the shared resource. If a shared resource is in RLock then it can be called again safely. The RLocked resource can be accessed repeatedly by various threads, though it still works correctly when called by different threads.

# Semaphore - Synchronization Primitives In Python

## Overview:

-   A semaphore is a synchronization construct.
-   Semaphore provides threads with synchronized access to a limited number of resources.
-   A semaphore is just a variable. The variable reflects the number of currently available resources. For example, a parking lot with a display of number of available slots on a specific level of a shopping mall is a semaphore.
-   The value of semaphore cannot go less than zero and greater then the total number of the available resources.
-   The semaphore is associated with two operations –  **acquire**  and  **release**.
-   When one of the resources synchronized by a semaphore is "**acquired**" by a thread, the value of the semaphore is decremented.
-   When one of the resources synchronized by a semaphore is "**released**" by a thread the value of the semaphore is incremented.
-   The Dutch computer scientist Edsger Dijkstra invented the concept of semaphore.
-   Dijkstra named the two operations on a semaphore acquire and release as p and v using the first letter of the Dutch words proberen and vehogen.
-   The word proberen means test and vehogen means increment in Dutch.

## Semaphores in Python:

-   The Semaphore class of the Python  threading  module implements the concept of semaphore.
-   It has a constructor and two methods  acquire()  and  release().
-   The  acquire() method decreases the semaphore count if the count is greater than zero. Else it blocks till the count is greater than zero.
-   The  release() method increases the semaphore count and wakes up one of the threads waiting on the semaphore.


# [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")  — Process-based parallelism[¶](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "Permalink to this headline")
**What is multiprocessing?**

Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.

**Why multiprocessing?**

Consider a computer system with a single processor. If it is assigned several processes at the same time, it will have to interrupt each task and switch briefly to another, to keep all of the processes going.

The  `multiprocessing`  module allows the programmer to fully leverage multiple processors on a given machine. The API used is similar to the classic  `threading`  module. It offers both local and remote concurrency.

The multiprocesing module avoids the limitations of the Global Interpreter Lock (GIL) by using subprocesses instead of threads. The multiprocessed code does not execute in the same order as serial code. There is no guarantee that the first process to be created will be the first to complete.

**Communication between processes**

Effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated.  
**multiprocessing**  supports two types of communication channel between processes:

-   Queue
-   Pipe

1.  **Queue :** A simple way to communicate between process with multiprocessing is to use a Queue to pass messages back and forth. Any Python object can pass through a Queue.  
    **Note:**  The  **multiprocessing.Queue**  class is a near clone of  [**queue.Queue**](https://docs.python.org/3/library/queue.html).
    
**Pipes :** A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required.

**multiprocessing**  module provides  **Pipe()**  function which returns a pair of connection objects connected by a pipe. The two connection objects returned by  **Pipe()**  represent the two ends of the pipe. Each connection object has  **send()**  and  **recv()**  methods (among others).

**Synchronization between processes**

Process synchronization is defined as a mechanism which ensures that two or more concurrent processes do not simultaneously execute some particular program segment known as  **critical section**.

Concurrent accesses to shared resource can lead to  **race condition**.

> A race condition occurs when two or more processes can access shared data and they try to change it at the same time. As a result, the values of variables may be unpredictable and vary depending on the timings of context switches of the processes.

**multiprocessing**  module provides a  **Lock**  class to deal with the race conditions.  **Lock**  is implemented using a  **Semaphore**  object provided by the Operating System.

> A semaphore is a synchronization object that controls access by multiple processes to a common resource in a parallel programming environment. It is simply a value in a designated place in operating system (or kernel) storage that each process can check and then change. Depending on the value that is found, the process can use the resource or will find that it is already in use and must wait for some period before trying again. Semaphores can be binary (0 or 1) or can have additional values. Typically, a process using semaphores checks the value and then, if it using the resource, changes the value to reflect this so that subsequent semaphore users will know to wait.

In order to utilize all the cores, **multiprocessing** module provides a **Pool** class. The **Pool** class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways.

-   We create a  **Pool**  object using:
    
    ```
      p = multiprocessing.Pool()
    
    ```
    
    There are a few arguments for gaining more control over offloading of task. These are:
    
    -   **processes:**  specify the number of worker processes.
    -   **maxtasksperchild:**  specify the maximum number of task to be assigned per child.
    
    All the processes in a pool can be made to perform some initialization using these arguments:
    
    -   **initializer:**  specify an initialization function for worker processes.
    -   **initargs:**  arguments to be passed to initializer.
-   Now, in order to perform some task, we have to map it to some function. In the example above, we map  **mylist**  to  **square**  function. As a result, the contents of  **mylist**  and definition of  **square**  will be distributed among the cores.
    
    ```
      result = p.map(square, mylist)
    
    ```
    
-   Once all the worker processes finish their task, a list is returned with the final result.
