/*
== lemons - Data visualization module ==

The "lemons" module is a data visualization module
created by Elis Staaf. Please take a look at the function list
below:


*/

package lemons

import (
  "fmt"
)

func table(slice []string) {
  for idx, val := range slice {
     fmt.Printf("%v\t%v\n", idx, val)
  }
}
