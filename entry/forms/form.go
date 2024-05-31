package forms

import (
	"encoding/json"
	"os"
)

type field string

type form interface {
	Build(onFile bool, idx int) string
}

func FillForm(jsonPath string, form form) {

	bytes, err := os.ReadFile(jsonPath)
	if err != nil {
		panic(err)
	}

	if err := json.Unmarshal(bytes, &form); err != nil {
		panic(err)
	}
}
