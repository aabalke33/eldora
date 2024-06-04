package ein

import (
	"io"
	"os"
)

const filePath = "C:/DRAKE23/DBF/EIN_DB"

type Eins struct {
	Eins map[string]bool
}

func NewEins() *Eins {
	e := Eins{}
	e.Eins = make(map[string]bool)
	return &e
}

/*
Parse Eins from EIN_DB Drake File
*/
func (Eins *Eins) ReadDb() {

	file, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}

	defer file.Close()

	// Ein length 9, DB chunk 256
	const chunkSize = 256
	const readSize = 9

	buffer := make([]byte, readSize)
	offset := int64(0)

	for {

		_, err := file.Seek(offset, io.SeekStart)
		if err != nil {
			panic(err)
		}

		if _, err = file.Read(buffer); err != nil {
			if err.Error() == "EOF" {
				break
			}
			panic(err)
		}

		Eins.Eins[string(buffer)] = true

		offset += chunkSize
	}
}

/*
Add Eins as ahk script compiler runs, to avoid state mismatches between forms
ex. if new ein, and first form enters, second form with same ein need to skip
extra data
*/
func (Eins *Eins) Add(ein string) {
	Eins.Eins[ein] = true
}
