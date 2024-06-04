package forms

type Ssa struct {
	Script               string
	Tsj                  field `json:"tsj"`
	F                    field `json:"f"`
	State                field `json:"state"`
	NetBenefits          field `json:"net_benefits"`
	MedicarePremiums     field `json:"medicare-premiums"`
	PremiumsSelfEmployed field `json:"premiums_self_employed"`
	Withholding          field `json:"withholding"`
	Designation          field `json:"designation"`
	NonTaxable           field `json:"nontaxable"`
	WorkersCompensation  field `json:"workers_compensation"`
}

func (ssa *Ssa) Build(onFile bool) (script string) {

	var fields []field

	fields = append(
		fields,
		ssa.Tsj,
		ssa.F,
		ssa.State,
		ssa.NetBenefits,
		ssa.MedicarePremiums,
		ssa.PremiumsSelfEmployed,
		ssa.Withholding,
		ssa.Designation,
		ssa.NonTaxable,
		ssa.WorkersCompensation,
	)

	existEntryWin := "Existing Forms List - SSA: SSA-1099, Social Security"
	script += openFormEntryWindow("SSA", existEntryWin)
	script += fillEntryWindow(fields)
	script += closeFormEntryWindow()
	return script
}

func (ssa *Ssa) GetTin() (payerTin field) {
	return field("")
}
