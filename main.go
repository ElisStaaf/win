package main

import (
    "fmt"
    "log"
)

func main() int {
    var msg string = "Hello World!\n"
    _, err := fmt.Printf(msg)
    if err != nil {
        log.Fatal("_SYSTEM_EXIT_FAIL: %s", err)
    }
    return 0
}
