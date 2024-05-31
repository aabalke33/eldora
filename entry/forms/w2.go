package forms

type W2 struct {
	Ts                    field `json:"ts"`
	F                     field `json:"f"`
	SpecialTaxTreatment   field `json:"special_tax_treatment"`
	Ein                   field `json:"ein"`
	EmployerName          field `json:"employer_name"`
	EmployerNameCont      field `json:"employer_name_cont"`
	EmployerStreet        field `json:"employer_street"`
	EmployerCity          field `json:"employer_city"`
	EmployerState         field `json:"employer_state"`
	EmployerZip           field `json:"employer_zip"`
	EmployeeFirst         field `json:"employee_first"`
	EmployeeLast          field `json:"employee_last"`
	EmployeeStreet        field `json:"employee_street"`
	EmployeeCity          field `json:"employee_city"`
	EmployeeState         field `json:"employee_state"`
	EmployeeZip           field `json:"employee_zip"`
	Wages                 field `json:"1"`
	Withholding           field `json:"2"`
	SocialWages           field `json:"3"`
	SocialWithholding     field `json:"4"`
	MedicareWages         field `json:"5"`
	MedicareWithholding   field `json:"6"`
	SocialTips            field `json:"7"`
	AllocatedTips         field `json:"8"`
	DependentCareBenefits field `json:"10"`
	NonqualifiedPlans     field `json:"11"`
	Box121Code            field `json:"12_1_code"`
	Box121Amount          field `json:"12_1_amount"`
	Box121Year            field `json:"12_1_year"`
	Box122Code            field `json:"12_2_code"`
	Box122Amount          field `json:"12_2_amount"`
	Box122Year            field `json:"12_2_year"`
	Box123Code            field `json:"12_3_code"`
	Box123Amount          field `json:"12_3_amount"`
	Box123Year            field `json:"12_3_year"`
	Box124Code            field `json:"12_4_code"`
	Box124Amount          field `json:"12_4_amount"`
	Box124Year            field `json:"12_4_year"`
	Statutory             field `json:"13_statutory"`
	Retirement            field `json:"13_retirement"`
	Sick                  field `json:"13_sick"`
	Other1                field `json:"14_1"`
	Other1Amount          field `json:"14_1_amount"`
	Other2                field `json:"14_2"`
	Other2Amount          field `json:"14_2_amount"`
	Other3                field `json:"14_3"`
	Other3Amount          field `json:"14_3_amount"`
	Other4                field `json:"14_4"`
	Other4Amount          field `json:"14_4_amount"`
	State1                field `json:"state_1"`
	State1Id              field `json:"state_1_id"`
	State1Wages           field `json:"state_1_wages"`
	State1Withholding     field `json:"state_1_withholding"`
	Local1Wages           field `json:"local_1_wages"`
	Local1Withholding     field `json:"local_1_withholding"`
	Local1Name            field `json:"local_1_name"`
	State2                field `json:"state_2"`
	State2Id              field `json:"state_2_id"`
	State2Wages           field `json:"state_2_wages"`
	State2Withholding     field `json:"state_2_withholding"`
	Local2Wages           field `json:"local_2_wages"`
	Local2Withholding     field `json:"local_2_withholding"`
	Local2Name            field `json:"local_2_name"`
	State3                field `json:"state_3"`
	State3Id              field `json:"state_3_id"`
	State3Wages           field `json:"state_3_wages"`
	State3Withholding     field `json:"state_3_withholding"`
	Local3Wages           field `json:"local_3_wages"`
	Local3Withholding     field `json:"local_3_withholding"`
	Local3Name            field `json:"local_3_name"`
	State4                field `json:"state_4"`
	State4Id              field `json:"state_4_id"`
	State4Wages           field `json:"state_4_wages"`
	State4Withholding     field `json:"state_4_withholding"`
	Local4Wages           field `json:"local_4_wages"`
	Local4Withholding     field `json:"local_4_withholding"`
	Local4Name            field `json:"local_4_name"`
	Nonstandard           field `json:"nonstandard"`
	Corrected             field `json:"corrected"`
	DoNotUpdate           field `json:"do_not_update"`
	Tin                   field `json:"tin"`
	Agent                 field `json:"agent"`
}

func (W2 *W2) Build(onFile bool, idx int) (output string) {

	var fields []field

	fields = append(fields, W2.Ts)
	fields = append(fields, W2.F)
	fields = append(fields, W2.SpecialTaxTreatment)
	fields = append(fields, W2.Ein)

	if !onFile {
		fields = append(fields, W2.EmployerName)
		fields = append(fields, W2.EmployerNameCont)
		fields = append(fields, W2.EmployerStreet)
		fields = append(fields, W2.EmployerCity)
		fields = append(fields, W2.EmployerState)
		fields = append(fields, W2.EmployerZip)
		fields = append(fields, W2.EmployeeFirst)
		fields = append(fields, W2.EmployeeLast)
		fields = append(fields, W2.EmployeeStreet)
		fields = append(fields, W2.EmployeeCity)
		fields = append(fields, W2.EmployeeState)
		fields = append(fields, W2.EmployeeZip)
	}

	fields = append(fields, W2.Wages)
	fields = append(fields, W2.Withholding)
	fields = append(fields, W2.SocialWages)
	fields = append(fields, W2.SocialWithholding)
	fields = append(fields, W2.MedicareWages)
	fields = append(fields, W2.MedicareWithholding)
	fields = append(fields, W2.SocialTips)
	fields = append(fields, W2.AllocatedTips)
	fields = append(fields, W2.DependentCareBenefits)
	fields = append(fields, W2.NonqualifiedPlans)
	fields = append(fields, W2.Box121Code)
	fields = append(fields, W2.Box121Amount)
	fields = append(fields, W2.Box121Year)
	fields = append(fields, W2.Box122Code)
	fields = append(fields, W2.Box122Amount)
	fields = append(fields, W2.Box122Year)
	fields = append(fields, W2.Box123Code)
	fields = append(fields, W2.Box123Amount)
	fields = append(fields, W2.Box123Year)
	fields = append(fields, W2.Box124Code)
	fields = append(fields, W2.Box124Amount)
	fields = append(fields, W2.Box124Year)
	fields = append(fields, W2.Statutory)
	fields = append(fields, W2.Retirement)
	fields = append(fields, W2.Sick)
	fields = append(fields, W2.Other1)
	fields = append(fields, W2.Other1Amount)
	fields = append(fields, W2.Other2)
	fields = append(fields, W2.Other2Amount)
	fields = append(fields, W2.Other3)
	fields = append(fields, W2.Other3Amount)
	fields = append(fields, W2.Other4)
	fields = append(fields, W2.Other4Amount)
	fields = append(fields, W2.State1)
	fields = append(fields, W2.State1Id)
	fields = append(fields, W2.State1Wages)
	fields = append(fields, W2.State1Withholding)
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, W2.State2)
	fields = append(fields, W2.State2Id)
	fields = append(fields, W2.State2Wages)
	fields = append(fields, W2.State2Withholding)
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, W2.State3)
	fields = append(fields, W2.State3Id)
	fields = append(fields, W2.State3Wages)
	fields = append(fields, W2.State3Withholding)
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, W2.State4)
	fields = append(fields, W2.State4Id)
	fields = append(fields, W2.State4Wages)
	fields = append(fields, W2.State4Withholding)
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, "")
	fields = append(fields, W2.Nonstandard)
	fields = append(fields, W2.Corrected)
	fields = append(fields, W2.DoNotUpdate)
	fields = append(fields, W2.Tin)
	fields = append(fields, W2.Agent)

	output += "W2{Enter}"

	for i := 0; i < idx; i++ {
		output += "{PgDn}{PgDn}"
	}

	for _, field := range fields {
		output += string(field) + "{Tab}"
	}

	output += "{Esc}"

	return output
}
