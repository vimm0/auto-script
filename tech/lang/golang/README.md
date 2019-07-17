##### Variable
- Variable Declaration
    - var foo int
    - var foo int = 42
    - foo := 42
- Redeclaration and Shadowing(overriding)
        - can not redeclare variables, but can shadow them
        - All variable must be used meaning, variable if used only be declared else not (built-in refactoring feature)
- Visibility
    - lower case first letter for package scope
    - upper case first letter to export
    - no private scope at all
- Naming Convention
    - Pascal or camelCase
        - Capitalize acronyms (HTTP, URL)
    - As short as reasonable
        - longer names for longer lives
- Type Conversions
    - destinationType(variable)
    - act as function conversion and convert in target value
    - use strconv package for strings conversion

##### Primitive
- Boolean Type
    - values are true or false
    - not an alias for other types(eg. int)
    - zero value is false
- Numeric Type
    - Integers
        - Signed Integer
            - int type has varying size, but min 32 bits
            - 8 bit(int8) through 64 bit(int64)
            - int8: 128 - 127
            - int16: 32768 - 32767
            - int32
            - int64
        - Unsigned Integer
            - 8bit(byte and uint8) through 32 bit(uint32)
            - uint8
            - uint16
            - uint32
        - Arithmetic Operator
            - Addition, Subtraction, Multiplication, Division, Reminder
        - Bitwise Operator
            - And, OR, XOR and NOT
        - zero value is zero
        - can't mix types in same family(uint64 + uint32= error)
    - Floating Point
        - Follow IEEE754 standard
        - zero value is 0
        - float32, float64
        - literal styles
            - decimal(3.45)
            - exponential(12e12 oe 2E10)
            - Mixed(13.7e12)
        - Arithmetic Operator
            - Addition, Subtraction, Multiplication, Division
    - Complex Number
        - zero value is (0+0i)
        - complex64
        - complex128
        - built-in functions
            - complex - make complex number from two floats
            - real - get real part as float
            - imag - get imaginary part as float
- Text Type
    - Strings
        - utf-8
        - immutable
        - can be concatenated with plus(+) operator
        - can be converted to []byte
    - Rune
        - utf-32
        - alias for int32
        - special method normally required to process
            - eg. strings, Reader#ReadRune        
##### Constant

- Naming convention
    - Immutable, but can be shadowed
    - Replaced by the compiler at compile time
        - Value must be calculable at compile time
    - Named like variables
        - PascalCase for exported constants
        - camelCase for internal constants
- Typed constants
    - Typed constants work like immutable variables
        - can interoperate only with same type
- Untyped constants
    - Untyped constant work like literals
        - can interoperate with similar types
- Enumerated constants
    - special symbol iota allows related constants to be created easily
    - Iota start at 0 in each const block and increments by one
    - watch out of constant value that match zero values for variables
- Enumerated expressions
    - Operations that can be determined at compile time are allowed
        - Arithmetic
        - Bitwise Operations
        - Bit shifting
        
##### Array and Slices
- Arrays
    - collection of items with same type
    - fixed size
    - declaration style
        - a := [3]int{1,2,3}
        - a := [...]int{1,2,3}
        - car a [3]int
    - Access via zero-based index
        - a := [3]int {1,2,3} // a[1] == 3
    - len function returns size of array
    - copies refer to different underlying data
- Slices
    - backed by array
    - Creation Stylle
        - slice existing array or slice
        - literal style
        - via make function
            - a:= make([]int, 10)
            - a:= make([]int, 10, 100)
        - len function return length of slice
        - cap function returns length of underlying array
        - append function to add elements to slice
            - may cause expensive copy operation if underlying array is too small
        - copies refer to same underlying array
        
##### Maps and Structs
- Maps
    - Collection of value types that are accessed via keys
    - Created via literals or via make function
    - Member accessed via [key] syntax
        - myMap["key"] = "value"
    - Check for presence with "value, ok" form of result
    - Multiple assignments refer to same underlying data
- Structs
    - Collection of disparate data types that describe a single concept
    - Keyed by named fields
    - Normally, created as types, but anonymous structs are allowed
    - Structs are value types
    - No inheritance, but can use composition via embedding
    - Tags can be added to struct fields to describe field
    
#### Control Flow 
##### (If and Switch Statement) 
- If statement
    - Initializer
    - Comparison operator
    - Logical operator
    - Short circuiting
    - If-else statements
    - If-else if statements
    - Equality and floats
- Switch statement
    - Switching on a tag
    - Cases with multiple tests
    - Initializers
    - Switches with no tag
    - Fallthrough (implicit break in go lang)
    - Type switches
    - Breaking out early (break in switch case)

##### Looping
    - For statement
        - simple loops
            - for initializer; test; incrementer {}
            - for test {}
            - for {}
        - exiting early
            - break
            - continue
            - labels
        - looping through collections
            - arrays, slice, maps, strings, channels
            - for k, v := range collection {}
##### Defer, Panic and Recovery
    - Defer
        - used to delay execution of a statement until function exists
        - useful to group "open" and "close" functions together
            - Be careful in loops
        - Run in LIFO(last-in, first-out) order
        - Arguments evaluated at time defer is executed, not at time of called function execution
    - Panic
        - occur when program cannot continue at all
            - Don't use when file can't be opened, unless it is critical
            - Use for unrecoverable events - cannot obtain TCP port for web server
        - function will stop executing
            - deferred function will still fire
        - If nothing handles panic, program will exit
    - Recover
        - used to recover from panics
        - only useful in defered functions (because in panic execution will stop immediately)
        - current function will not attempt to continue, but higher functions in call stack will

##### Pointers
    - creating pointers
        - Pointer types use an asterisk (*) as a prefix to type pointed to
            - *int - a pointer to an integer
        - Use the addressof operator (&) to get address of variable
    - deferencing pointers
        - dereference a pointer by preceding with an asterisk(*)
        - complex types (eg. structs) are automatically dereferenced
    - create pointers to objects
        - can use the addressof operator (&) if value type already exists
            - ms := myStruct{foo: 42}
            - p := &ms
        - use addressof operator before initializer
            - &myStruct{foo: 42}
        - use the new keyword
            - can't initialize fields at the same time
    - the new function
    - working with nil
    - types with internal pointers
        - All assignment operatiions in Go are copy operations
        - Slice and maps contains internal pointers, so copies point to same underlying data
##### Functions
- Basic Syntax
    - func foo(){
        ...
    }
    - lowercase name in function indicate private
    - uppercase name in function indicate public
- Parameters
    - comma delimited list of variables and types
        - func foo(bar string, baz int)
    - parameters of same type list type once
        - func foo(bar, baz int)
    - when pointers are passed in, the function can change the value in the caller
        - This is always true for data of slice and maps
    - use variadic parameters to send list of same types in
        - must be last parameter
        - received as a slice
        - func foo(bar string, baz ...int)
- Return Values
    - single return values just like type
        - func foo() int
    - multiple return value list type surrounded by parentheses
        - func foo() (int, error)
        - The (result type, error) paradigm in a very common idiom
    - can use named return values
        - initializes returned values
        - return using return keyword on its own
    - can return addresses of local variables
        - automatically promoted from local memory (stack) to shared memory (heap)
- Anonymous Functions
    - Function don't have names if they are:
        - immediately invoked
            - func() {
                ...
            }()
        - assigned to a variable or passed as an argument to a function
            - a := func() {
                ...
            }
            a()
- Functions as types
    - can assigni function to variables or use as arguments and return values in functions
    - Type signature is like function signature, with no parameter names
        - var f func(string, string, int) (int, error)
- Methods
    - function that executes in context of a type
    - format
        - func (g greeter) greet() {
            ...
        }
    - receiver can be value or pointer
        - value receiver gets copy of type
        - pointer receiver gets pointer to type
        
##### Interfaces
- Basics
    - type Writer interface {
        Write([]byte)(int, error)
    }
    type ConsoleWriter struct {}
    func (cw ConsoleWriter) Write(data []byte)(int, error){
        n, err := fmt.Println(String(data))
        return n, err
    }
- composing interface
    - type Writer interface {
        Write([]byte)(int, error)
    }
    type Closer interface {
        Close()error
    }
    type WriterCloser interface{
        Writer
        Closer
    }
- type conversion
    - var wc WriterCloser = NewBufferedWriterCloser()
      bwc := wc.(*BufferedWriterCloser)
    - the empty interface
        - var i interface{} = 0
    - type switches
        - var i interface{} = 0
          switch i.(type) {
              case int:
                fmt.Println("i is integer")
              case string:
                fmt.Println("i is string")
              default:
                fmt.Println("I don't know what i is")
          }
- implementing with values vs pointers
    - method set of value is all methods with value receivers
    - method set of pointer is all methods, regardless of receiver type
- best practices
    - use many, small interfaces
        - single method interfaces are some of the most powerful and flexible
            - io.Writer, io.Reader, interface{}
    - don't export interfaces for types that will be consumed
    - do export interfaces for types that will be used by package
    - design functions and methods to receive interfaces whenever possible
##### GOROUTINE
- creating goroutines
    - use go keyword in front of function call
    - when using anonymous function, pass data as local variables.
- synchronization
    - waitgroups
        - use sync.WaitGroup to wait for groups of goroutines to complete
    - mutexes
        - use sync.Mutex and sync.RWMutex to protect data access
- parallelism
    - by default, go will use CPU threads equal to available cores
    - change with runtime.GOMAXPROC
    - more threads can increase prformance, but too many can slow it down
- best practices
    - dont create goroutines in library
        - let consumer control concurrency
    - when creating a goroutine, know how it will end
        - Avoid subtle memory leaks
    - check for race condition at compile time

##### channels
- channel basics
    - create a channel with make command
         - make(chan int)
    - send message in to channel 
        - ch <- val
    - receive message from channel
        - val := <-ch
    - can have multiple senders and receivers
- restriction data flow
    - channel can be cast into send-only or receive only versions
        - send-only: chan <- int
        - receive-only: <- chan int
- buffered channels
    - channels block sender side till receiver is available
    - block receiver side till message is available
    - can decouple sender and receiver with buffered channels
        - make (chan int, 50)
    - use buffered channels when send and receiver have assymmetric loading
- closing channels
- for...range loop with channels
    - use to monitor channel and process messages as they arrive
    - loop exits when channel is closed
- select statement
    - allow goroutine to monitor several channels at once
        - block if all channels block
        - if multiple channel receive value simultaneously, behavior is undefined

###### Reference
- [Learn Go Programming - Golang Tutorial for Beginners](https://www.youtube.com/watch?v=YS4e4q9oBaU&t=1206s)
- [Concurrency in Go](https://www.youtube.com/watch?v=LvgVSSpwND8)
- [Live building a scalable API in Go with Kubernetes](https://www.youtube.com/watch?v=pkZrgHxJ130)
- [Creating a Go API using an ORM - Tutorial](https://www.youtube.com/watch?v=VAGodyl84OY)
- [why Golang is Sucessful by Creator of Golang Rob-pike](https://www.youtube.com/watch?v=cQ7STILAS0M)
- [Go for Pythonistas](https://www.youtube.com/watch?v=elu0VpLzJL8)