package forms

type Div struct {
	Script                   string
	Tsj                      field `json:"tsj"`
	F                        field `json:"f"`
	St                       field `json:"st"`
	DoNotUpdate              field `json:"do_not_update"`
	PayerTin                 field `json:"payer_tin"`
	SSN                      field `json:"ssn"`
	PayerName                field `json:"payer_name"`
	PayerStreet              field `json:"payer_street"`
	PayerCity                field `json:"payer_city"`
	PayerState               field `json:"payer_state"`
	PayerZip                 field `json:"payer_zip"`
	AccountNumber            field `json:"account_number"`
	Fatca                    field `json:"fatca"`
	OrdinaryDividends        field `json:"ordinary_dividends"`
	QualifiedDividends       field `json:"qualified_dividends"`
	CapitalGainDistribution  field `json:"capital_gain_distribution"`
	TwentyFivePercentRage    field `json:"twenty_five_percent_rate"`
	Section1202Quarter       field `json:"section_1202_quarter"`
	Section1202              field `json:"section_1202"`
	CollectiblesGain         field `json:"collectibles_gain"`
	Section897Dividends      field `json:"section_897_dividends"`
	Section897CapitalGain    field `json:"section_897_capital_gain"`
	NondividendDistribution  field `json:"nondividend_distribution"`
	Withholding              field `json:"withholding"`
	Section199ADividends     field `json:"section_199a_dividends"`
	InvestmentExpenses       field `json:"investment_expenses"`
	ForeignTaxPaid           field `json:"foreign_tax_paid"`
	ForeignCountry           field `json:"foreign_country"`
	CashLiquidation          field `json:"cash_liquidation"`
	NonCashLiquidation       field `json:"noncash_liquidation"`
	ExemptInterestDividends  field `json:"exempt_interest_dividends"`
	SpecifiedPrivateActivity field `json:"specified_private_activity"`
	State1                   field `json:"state_1"`
	State1Id                 field `json:"state_1_id"`
	State1Withholding        field `json:"state_1_withholding"`
	State2                   field `json:"state_2"`
	State2Id                 field `json:"state_2_id"`
	State2Withholding        field `json:"state_2_withholding"`
}

func (Div *Div) Build(onFile bool) (script string) {

	var fields []field

	fields = append(
		fields,
		Div.Tsj,
		Div.F,
		Div.St,
		Div.DoNotUpdate,
		Div.PayerTin,
	)

	if !onFile {
		fields = append(
			fields,
			Div.SSN,
			Div.PayerName,
			Div.PayerStreet,
			Div.PayerCity,
			Div.PayerState,
			Div.PayerZip,
		)
	}

	fields = append(
		fields,
		Div.AccountNumber,
		Div.Fatca,
		Div.OrdinaryDividends,
		Div.QualifiedDividends,
		Div.CapitalGainDistribution,
		Div.TwentyFivePercentRage,
		Div.Section1202Quarter,
		Div.Section1202,
		Div.CollectiblesGain,
		Div.Section897Dividends,
		Div.Section897CapitalGain,
		Div.NondividendDistribution,
		Div.Withholding,
		Div.Section199ADividends,
		Div.InvestmentExpenses,
		Div.ForeignTaxPaid,
		Div.ForeignCountry,
		Div.CashLiquidation,
		Div.NonCashLiquidation,
		Div.ExemptInterestDividends,
		Div.SpecifiedPrivateActivity,
		Div.State1,
		Div.State1Id,
		Div.State1Withholding,
		Div.State2,
		Div.State2Id,
		Div.State2Withholding,
	)

	existEntryWin := "Existing Forms List - DIV: 1099-DIV, Dividend Income"
	script += openFormEntryWindow("DIV", existEntryWin)
	script += fillEntryWindow(fields)
	script += closeFormEntryWindow()
	return script
}

func (Div *Div) GetTin() (payerTin field) {
	return Div.PayerTin
}
