package main

import (
    "bufio"
    "fmt"
    "os"
    "os/exec"
    "strings"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)

    fmt.Println("Goshell.go - Made by Elis Staaf.")
    fmt.Println("Type \"end\" to exit.\n")

    for {
        // Get the current working directory
        dir, err := os.Getwd()
        if err != nil {
            fmt.Fprintln(os.Stderr, "Error getting current directory:", err)
            continue
        }

        // Display the prompt with the current directory
        fmt.Printf("%s> ", dir) // Display current directory
        scanner.Scan()

        input := scanner.Text()
        if input == "end" {
            break // Exit the shell if user types "exit"
        }

        // Split input into command and arguments
        args := strings.Fields(input)
        if len(args) == 0 {
            continue // No command entered, prompt again
        }

        // Create command
        cmd := exec.Command(args[0], args[1:]...)

        // Get command output
        output, err := cmd.CombinedOutput()
        if err != nil {
            fmt.Fprintln(os.Stderr, "Error executing command:", err)
        }
        fmt.Print(string(output))
    }

    fmt.Println("Exiting the shell.")
}
