package forms

type G struct {
	Script                   string
	Tsj                      field `json:"tsj"`
	F                        field `json:"f"`
	Corrected                field `json:"corrected"`
	PayerTin                 field `json:"payer_tin"`
	PayerName                field `json:"payer_name"`
	PayerNameCont            field `json:"payer_name_cont"`
	PayerStreet              field `json:"payer_street"`
	PayerCity                field `json:"payer_city"`
	PayerState               field `json:"payer_state"`
	PayerZip                 field `json:"payer_zip"`
	PayerPhone               field `json:"payer_phone"`
	UnemploymentCompensation field `json:"unemployment_compensation"`
	UnemploymentRepaid       field `json:"unemployment_repaid"`
	StateRefunds             field `json:"state_refunds"`
	Standard2022             field `json:"standard_2022"`
	SalesTax2022             field `json:"sales_tax_2022"`
	TaxYear                  field `json:"tax_year"`
	Withholding              field `json:"withholding"`
	RtaaPayments             field `json:"rtaa_payments"`
	ForCode                  field `json:"for_code"`
	Mfc                      field `json:"mfc"`
	TaxableGrants            field `json:"taxable_grants"`
	Agriculture              field `json:"agriculture"`
	TradeBusiness            field `json:"trade_business"`
	MarketGain               field `json:"market_gain"`
	State                    field `json:"state"`
	StateId                  field `json:"state_id"`
	StateUnemployment        field `json:"state_unemployment"`
	StateWithholding         field `json:"state_withholding"`
	LocalPayment             field `json:"local_payment"`
	LocalWithholding         field `json:"local_withholding"`
	Locality                 field `json:"locality"`
}

func (g *G) Build(onFile bool) (script string) {

	var fields []field

	fields = append(
		fields,
		g.Tsj,
		g.F,
		g.Corrected,
		g.PayerTin,
	)

	if !onFile {
		fields = append(
			fields,
			g.PayerName,
			g.PayerNameCont,
			g.PayerStreet,
			g.PayerCity,
			g.PayerState,
			g.PayerZip,
			g.PayerPhone,
		)
	}

	fields = append(
		fields,
		g.UnemploymentCompensation,
		g.UnemploymentRepaid,
		g.StateRefunds,
		g.Standard2022,
		g.SalesTax2022,
		g.TaxYear,
		g.Withholding,
		g.RtaaPayments,
		g.ForCode,
		g.Mfc,
		g.TaxableGrants,
		g.Agriculture,
		g.TradeBusiness,
		g.MarketGain,
		g.State,
		g.StateId,
		g.StateUnemployment,
		g.StateWithholding,
		g.LocalPayment,
		g.LocalWithholding,
		g.Locality,
	)

	existEntryWin := "Existing Forms List - 99G: 1099-G, Government Payments"
	script += openFormEntryWindow("99G", existEntryWin)
	script += fillEntryWindow(fields)
	script += closeFormEntryWindow()
	return script
}

func (g *G) GetTin() (payerTin field) {
	return g.PayerTin
}
