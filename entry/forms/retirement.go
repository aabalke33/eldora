package forms

type Retirement struct {
	Script                    string
	Tsj                       field `json:"tsj"`
	F                         field `json:"f"`
	Type                      field `json:"type"`
	Corrected                 field `json:"corrected"`
	PayerTin                  field `json:"payer_tin"`
	PayerName                 field `json:"payer_name"`
	PayerStreet               field `json:"payer_street"`
	PayerCity                 field `json:"payer_city"`
	PayerState                field `json:"payer_state"`
	PayerZip                  field `json:"payer_zip"`
	PayerPhone                field `json:"payer_phone"`
	GrossDistribution         field `json:"gross_distribution"`
	Taxable                   field `json:"taxable"`
	NotDetermined             field `json:"not_determined"`
	TotalDistribution         field `json:"total_distribution"`
	CapitalGain               field `json:"capital_gain"`
	Withholding               field `json:"withholding"`
	EmployeeContribution      field `json:"employee_contribution"`
	UnrealizedAppreciation    field `json:"unrealized_appreciation"`
	DistributionCode1         field `json:"distribution_code_1"`
	DistributionCode2         field `json:"distribution_code_2"`
	IRA                       field `json:"ira"`
	Other                     field `json:"other"`
	OtherPercentage           field `json:"other_percentage"`
	TaxpayerPercent           field `json:"taxpayer_percent"`
	TotalEmployeeContribution field `json:"total_employee_contribution"`
	IrrAllocable              field `json:"irr_allocable"`
	FirstYearRoth             field `json:"first_year_roth"`
	Fatca                     field `json:"fatca"`
	State1Withholding         field `json:"state_1_withholding"`
	State1                    field `json:"state_1"`
	State1Id                  field `json:"state_1_id"`
	State1Distribution        field `json:"state_1_distribution"`
	Local1Withholding         field `json:"local_1_withholding"`
	Local1Distribution        field `json:"loca_l_1distribution"`
	State2Withholding         field `json:"state_2_withholding"`
	State2                    field `json:"state_2"`
	State2Id                  field `json:"state_2_id"`
	State2Distribution        field `json:"state_2_distribution"`
	Local2Withholding         field `json:"local_2_withholding"`
	Local2Distribution        field `json:"local_2_distribution"`
}

func (retirement *Retirement) Build(onFile bool) (script string) {

	var fields []field

	fields = append(
		fields,
		retirement.Tsj,
		retirement.F,
		retirement.Type,
		retirement.Corrected,
		retirement.PayerTin,
	)

	if !onFile {
		fields = append(
			fields,
			retirement.PayerName,
			retirement.PayerStreet,
			retirement.PayerCity,
			retirement.PayerState,
			retirement.PayerZip,
			retirement.PayerPhone,
		)
	}

	fields = append(
		fields,
		retirement.GrossDistribution,
		retirement.Taxable,
		retirement.NotDetermined,
		retirement.TotalDistribution,
		retirement.CapitalGain,
		retirement.Withholding,
		retirement.EmployeeContribution,
		retirement.UnrealizedAppreciation,
		retirement.DistributionCode1,
		retirement.DistributionCode2,
		retirement.IRA,
		retirement.Other,
		retirement.OtherPercentage,
		retirement.TaxpayerPercent,
		retirement.TotalEmployeeContribution,
		retirement.IrrAllocable,
		retirement.FirstYearRoth,
		retirement.Fatca,
		retirement.State1Withholding,
		retirement.State1,
		retirement.State1Id,
		retirement.State1Distribution,
		retirement.Local1Withholding,
		retirement.Local1Distribution,
		retirement.State2Withholding,
		retirement.State2,
		retirement.State2Id,
		retirement.State2Distribution,
		retirement.Local2Withholding,
		retirement.Local2Distribution,
	)

	existEntryWin := "Existing Forms List - 1099: 1099-R, Retirement"
	script += openFormEntryWindow("1099", existEntryWin)
	script += fillEntryWindow(fields)
	script += closeFormEntryWindow()
	return script
}

func (Retirement *Retirement) GetTin() (payerTin field) {
	return Retirement.PayerTin
}
