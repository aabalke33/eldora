package ein

import (
	"io"
	"os"
)

const filePath = "./data/EIN_DB"

type Eins map[string]bool

/*
   Parse Eins from EIN_DB Drake File
*/
func GetEins() (eins Eins) {

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

	eins = make(Eins)

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

		eins[string(buffer)] = true

		offset += chunkSize
	}

	return eins
}
