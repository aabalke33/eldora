package forms

type W2g struct {
	Script              string
	Ts                  field `json:"ts"`
	F                   field `json:"f"`
	MultiCode           field `json:"multicode"`
	PayerTin            field `json:"payer_tin"`
	PayerName           field `json:"payer_name"`
	PayerNameCont       field `json:"payer_namecont"`
	PayerStreet         field `json:"payer_street"`
	PayerCity           field `json:"payer_city"`
	PayerState          field `json:"payer_state"`
	PayerZip            field `json:"payer_zip"`
	PayerPhone          field `json:"payer_phone"`
	ReportableWinnings  field `json:"reportable_winnings"`
	DateWon             field `json:"date_won"`
	TypeOfWager         field `json:"type_of_wager"`
	Withholding         field `json:"withholding"`
	Transaction         field `json:"transaction"`
	Race                field `json:"race"`
	IdenticalWagerWin   field `json:"identical_wager_win"`
	Cashier             field `json:"cashier"`
	Window              field `json:"window"`
	FirstId             field `json:"first_id"`
	SecondId            field `json:"second_id"`
	State1              field `json:"state_1"`
	State1Id            field `json:"state_1_id"`
	StateWinnings       field `json:"state_winnings"`
	StateTaxWithholding field `json:"state_tax_withholding"`
	LocalWinnings       field `json:"local_winnings"`
	LocalWithholding    field `json:"local_withholding"`
	Locality            field `json:"locality"`
	Altered             field `json:"altered"`
	Corrected           field `json:"corrected"`
	LotteryWinnings     field `json:"lottery_winnings"`
	ElectronicGames     field `json:"electronic_games"`
	CostOfTicket        field `json:"cost_of_ticket"`
}

func (w2g *W2g) Build(onFile bool) (script string) {

	var fields []field
	fields = append(
		fields,
		w2g.Ts,
		w2g.F,
		w2g.MultiCode,
		w2g.PayerTin,
	)

	if !onFile {
		fields = append(
			fields,
			w2g.PayerName,
			w2g.PayerNameCont,
			w2g.PayerStreet,
			w2g.PayerCity,
			w2g.PayerState,
			w2g.PayerZip,
			w2g.PayerPhone,
		)
	}

	fields = append(
		fields,
		w2g.ReportableWinnings,
		w2g.DateWon,
		w2g.TypeOfWager,
		w2g.Withholding,
		w2g.Transaction,
		w2g.Race,
		w2g.IdenticalWagerWin,
		w2g.Cashier,
		w2g.Window,
		w2g.FirstId,
		w2g.SecondId,
		w2g.State1,
		w2g.State1Id,
		w2g.StateWinnings,
		w2g.StateTaxWithholding,
		w2g.LocalWinnings,
		w2g.LocalWithholding,
		w2g.Locality,
		w2g.Altered,
		w2g.Corrected,
		w2g.LotteryWinnings,
		w2g.ElectronicGames,
		w2g.CostOfTicket,
	)

	existEntryWin := "Existing Forms List - W2G: Gambling Income"
	script += openFormEntryWindow("W2G", existEntryWin)
	script += fillEntryWindow(fields)
	script += closeFormEntryWindow()
	return script
}

func (w2g *W2g) GetTin() (payerTin field) {
	return w2g.PayerTin
}
