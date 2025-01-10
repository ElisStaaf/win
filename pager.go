package main

import (
  "fmt"
  "os"
)

type Page struct {
    Title string
    Body  []byte
}

func (pager *Page) save() error {
    filename := pager.Title + ".txt"
    return os.WriteFile(filename, pager.Body, 0600)
}

func loadPage(title string) (*Page, error) {
    filename := title + ".txt"
    body, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }
    return &Page{Title: title, Body: body}, nil
}

func (pager *Page) get() {
  fmt.Printf(string(pager.Body))
}

func main() {
  pager := &Page{Title: "HelloWorld", Body: []byte("Hello, world!\n")}
  pager.save()
  pager.get()
}
