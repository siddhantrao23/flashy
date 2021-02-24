/*
Copyright © 2021 Siddhant Rao (raosiddhant99@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"fmt"
	"os"
	"os/exec"
	"strings"
	"bufio"

	"github.com/spf13/cobra"
)

func clear() {
	clear := exec.Command("clear")
	clear.Stdout = os.Stdout
	clear.Run()
}

var createCmd = &cobra.Command{
	Use:   "create",
	Short: "Create flashcards with a particular topic",
	Long: `Creates a flashcard set used for future practice.
Overwrites flashcards if the topic name already exists.

Synatx:
flashy create [topic]
`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if len(args) != 1 {
			return fmt.Errorf("the create command should have only one argument, the name of the topic of the flashcard set")
		}
		reader := bufio.NewReader(os.Stdin)
		file, _ := os.Create("." + args[0] + ".csv")

		clear()
		var num int
		fmt.Println("Enter the number of questions")
		fmt.Scanf("%d", &num)
		clear()

		writer := bufio.NewWriter(file)
		for a := 0; a < num; a++ {
			fmt.Println("*****************************************")
			fmt.Println("Enter the question!")
			fmt.Println("*****************************************")
			question, _ := reader.ReadString('\n')
			question = strings.TrimSuffix(question, "\n")
			fmt.Println("Enter the answer!")
			fmt.Println("*****************************************")
			answer, _ := reader.ReadString('\n')
			answer = strings.TrimSuffix(answer, "\n")

			writer.WriteString(question + "," + answer + "\n")
			clear()
		}
		writer.Flush()
		return nil
	},
}

func init() {
	rootCmd.AddCommand(createCmd)
}