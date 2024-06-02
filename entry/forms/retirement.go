package forms

type Retirement struct {
	Script                    string
	Tsj                       field `json:"tsj"`
	F                         field `json:"f"`
	Type                      field `json:"type"`
	Corrected                 field `json:"corrected"`
	PayerTIN                  field `json:"payer_tin"`
	PayerName                 field `json:"payer_name"`
	PayerStreet               field `json:"payer_street"`
	PayerCity                 field `json:"payer_city"`
	PayerState                field `json:"payer_state"`
	PayerZip                  field `json:"payer_zip"`
	PayerPhone                field `json:"payer_phone"`
	GrossDistribution         field `json:"gross_distribution"`
	Taxable                   field `json:"taxable"`
	NotDetermined             bool `json:"not_determined"`
	TotalDistribution         bool `json:"total_distribution"`
	CapitalGain               field `json:"capital_gain"`
	Withholding               field `json:"withholding"`
	EmployeeContribution      field `json:"employee_contribution"`
	UnrealizedAppreciation    field `json:"unrealized_appreciation"`
	DistributionCode1         field `json:"distribution_code_1"`
	DistributionCode2         field `json:"distribution_code_2"`
	IRA                       bool `json:"ira"`
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

    fields = append(fields, retirement.Tsj)
    fields = append(fields, retirement.F)
    fields = append(fields, retirement.Type)
    fields = append(fields, retirement.Corrected)
    fields = append(fields, retirement.PayerTIN)

    if !onFile {
        fields = append(fields, retirement.PayerName)
        fields = append(fields, retirement.PayerStreet)
        fields = append(fields, retirement.PayerCity)
        fields = append(fields, retirement.PayerState)
        fields = append(fields, retirement.PayerZip)
        fields = append(fields, retirement.PayerPhone)
    }

    fields = append(fields, retirement.GrossDistribution)
    fields = append(fields, retirement.Taxable)
    fields = append(fields, retirement.NotDetermined)
    fields = append(fields, retirement.TotalDistribution)
    fields = append(fields, retirement.CapitalGain)
    fields = append(fields, retirement.Withholding)
    fields = append(fields, retirement.EmployeeContribution)
    fields = append(fields, retirement.UnrealizedAppreciation)
    fields = append(fields, retirement.DistributionCode1)
    fields = append(fields, retirement.DistributionCode2)
    fields = append(fields, retirement.IRA)
    fields = append(fields, retirement.Other)
    fields = append(fields, retirement.OtherPercentage)
    fields = append(fields, retirement.TaxpayerPercent)
    fields = append(fields, retirement.TotalEmployeeContribution)
    fields = append(fields, retirement.IrrAllocable)
    fields = append(fields, retirement.FirstYearRoth)
    fields = append(fields, retirement.Fatca)
    fields = append(fields, retirement.State1Withholding)
    fields = append(fields, retirement.State1)
    fields = append(fields, retirement.State1Id)
    fields = append(fields, retirement.State1Distribution)
    fields = append(fields, retirement.Local1Withholding)
    fields = append(fields, retirement.Local1Distribution)
    fields = append(fields, retirement.State2Withholding)
    fields = append(fields, retirement.State2)
    fields = append(fields, retirement.State2Id)
    fields = append(fields, retirement.State2Distribution)
    fields = append(fields, retirement.Local2Withholding)
    fields = append(fields, retirement.Local2Distribution)

	existEntryWin := "Existing Forms List - 1099: 1099-R, Retirement"
	script += openFormEntryWindow("1099", existEntryWin)
	script += fillEntryWindow(fields)
	script += closeFormEntryWindow()
	return script
}
