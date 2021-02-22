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
	"bufio"
	"strings"
	"time"

	"github.com/spf13/cobra"
)

var practiceCmd = &cobra.Command{
	Use:   "practice",
	Short: "Pratice your premade flashcards",
	Long: `Given the name of the flashcard set, user can practice the set in two modes
-l, --linear   : for practicing in the order that the set was created in
-s, --shuffle  : for practicing the set in shuffled order`,
	Run: func(cmd *cobra.Command, args []string) {
		clear()
		lin, _ := cmd.Flags().GetString("linear")
		shuff, _ := cmd.Flags().GetString("shuffle")

		if shuff == "" {
			// linear called
			file, _ := os.Open("." + lin + ".csv")
			scanner := bufio.NewScanner(file)
			for scanner.Scan() {
				qna := strings.Split(scanner.Text(), ",")
				ques := qna[0]
				ans := qna[1]
				fmt.Println("*****************************************")
				fmt.Println(ques + "?")
				fmt.Println("*****************************************")
				reader := bufio.NewReader(os.Stdin)
				answer, _ := reader.ReadString('\n')
				answer = strings.TrimSuffix(answer, "\n")
				clear()
				if (strings.Compare(answer, ans) == 0) {
					fmt.Println("*****************************************")
					fmt.Println("Correct answer!!")
					fmt.Println("*****************************************")
					time.Sleep(2 * time.Second)
				} else {
					fmt.Println("*****************************************")
					fmt.Println("Wrong answer! :(")
					fmt.Println("*****************************************")
					fmt.Println("The correct answer was \n" + ans)
					fmt.Println("*****************************************")
					time.Sleep(2 * time.Second)
				}
				clear()
			}
			file.Close()
		}
		if lin == "" {
			// shuffle called
			file, _ := os.Open("." + shuff + ".csv")
			scanner := bufio.NewScanner(file)
			for scanner.Scan() {
				fmt.Println(scanner.Text())
			}
			file.Close()
		}
	},
}

func init() {
	rootCmd.AddCommand(practiceCmd)
	practiceCmd.Flags().StringP(
		"linear",
		"l",
		"",
		"topic of the flashcard set")
	practiceCmd.Flags().StringP(
		"shuffle",
		"s",
		"",
		"topic of the flashcard set")
}
