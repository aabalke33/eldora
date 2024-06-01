package forms

type Int struct {
	Script                         string
	Tsj                            field `json:"tsj"`
	F                              field `json:"f"`
	St                             field `json:"st"`
	SellerFinancedMortgage         field `json:"seller_financed_mortgage"`
	DoNotUpdate                    field `json:"do_not_update"`
	PayerTIN                       field `json:"payer_tin"`
	SSN                            field `json:"ssn"`
	PayerName                      field `json:"payer_name"`
	PayerStreet                    field `json:"payer_street"`
	PayerCity                      field `json:"payer_city"`
	PayerState                     field `json:"payer_state"`
	PayerZip                       field `json:"payer_zip"`
	AccountNumber                  field `json:"account_number"`
	RtnNumber                      field `json:"rtn_number"`
	Fatca                          field `json:"fatca"`
	Interest                       field `json:"interest"`
	EarlyWithdrawalPenalty         field `json:"early_withdrawal_penalty"`
	UsGovermentInterest            field `json:"us_govt_interest"`
	Withholding                    field `json:"withholding"`
	InvestmentExpenses             field `json:"investment_expenses"`
	ForeignTaxPaid                 field `json:"foreign_tax_paid"`
	ForeignCountry                 field `json:"foreign_country"`
	TaxExemptInterest              field `json:"tax_exempt_interest"`
	PrivateActivityBondInterest    field `json:"private_activity_bond_interest"`
	MarketDiscount                 field `json:"market_discount"`
	BondPremiumAmortizable         field `json:"bond_premium_amortizable"`
	BondPremiumTreasuryObligations field `json:"bond_premium_treasury_obligations"`
	BondPremiumTaxExempt           field `json:"bond_premium_tax_exempt"`
	TaxExemptCusip                 field `json:"tax_exempt_cusip"`
	State1                         field `json:"state_1"`
	State1Id                       field `json:"state_1_id"`
	State1Withholding              field `json:"state_1_withholding"`
	State2                         field `json:"state_2"`
	State2Id                       field `json:"state_2_id"`
	State2Withholding              field `json:"state_2_withholding"`
	NomineeInterest                field `json:"nominee_interest"`
	AccruedInterest                field `json:"accrued_interest"`
	NonTaxableOidInterest          field `json:"nontaxable_oid_interest"`
	ForeignInterest                field `json:"foreign_interest"`
	Form1116Required               field `json:"form_1116_required"`
}

func (Int *Int) Build(onFile bool) (script string) {

	var fields []field

	fields = append(fields, Int.Tsj)
	fields = append(fields, Int.F)
	fields = append(fields, Int.St)
	fields = append(fields, Int.SellerFinancedMortgage)
	fields = append(fields, Int.DoNotUpdate)
	fields = append(fields, Int.PayerTIN)

    if !onFile {
        fields = append(fields, Int.SSN)
        fields = append(fields, Int.PayerName)
        fields = append(fields, Int.PayerStreet)
        fields = append(fields, Int.PayerCity)
        fields = append(fields, Int.PayerState)
        fields = append(fields, Int.PayerZip)
    }

	fields = append(fields, Int.AccountNumber)
	fields = append(fields, Int.RtnNumber)
	fields = append(fields, Int.Fatca)
	fields = append(fields, Int.Interest)
	fields = append(fields, Int.EarlyWithdrawalPenalty)
	fields = append(fields, Int.UsGovermentInterest)
	fields = append(fields, Int.Withholding)
	fields = append(fields, Int.InvestmentExpenses)
	fields = append(fields, Int.ForeignTaxPaid)
	fields = append(fields, Int.ForeignCountry)
	fields = append(fields, Int.TaxExemptInterest)
	fields = append(fields, Int.PrivateActivityBondInterest)
	fields = append(fields, Int.MarketDiscount)
	fields = append(fields, Int.BondPremiumAmortizable)
	fields = append(fields, Int.BondPremiumTreasuryObligations)
	fields = append(fields, Int.BondPremiumTaxExempt)
	fields = append(fields, Int.TaxExemptCusip)
	fields = append(fields, Int.State1)
	fields = append(fields, Int.State1Id)
	fields = append(fields, Int.State1Withholding)
	fields = append(fields, Int.State2)
	fields = append(fields, Int.State2Id)
	fields = append(fields, Int.State2Withholding)
	fields = append(fields, Int.NomineeInterest)
	fields = append(fields, Int.AccruedInterest)
	fields = append(fields, Int.NonTaxableOidInterest)
	fields = append(fields, Int.ForeignInterest)

	existEntryWin := "Existing Forms List - INT: 1099-INT, Interest Income"
	script += openFormEntryWindow("INT", existEntryWin)
	script += fillEntryWindow(fields)

	if Int.ForeignTaxPaid != "" {
		script += "{Space}"

	}
	script += closeFormEntryWindow()
	return script
}
