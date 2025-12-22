package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	err := renameFile("renaming/txt")
	if err != nil {
		fmt.Println("ERROR")
	}
}

func renameFile(d string) error {
	files, err := os.ReadDir(d)
	if err != nil {
		fmt.Println("Error reading directory:", err)
		return err
	}
	count := 1
	for _, file := range files {
		if file.IsDir() {
			continue
		}
		oldPath := filepath.Join(d, file.Name())
		extension := filepath.Ext(file.Name())
		newName := fmt.Sprintf("file_%03d%s", count, extension)
		newPath := filepath.Join(d, newName)
		err := os.Rename(oldPath, newPath)
		if err != nil {
			return err
		}
	}
	return nil
}
