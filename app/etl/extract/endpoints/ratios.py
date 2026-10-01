from app.etl.extract.base_client import FMPClient

class Ratios(FMPClient):
    def __init__(self, api_key, symbol=None, date=None, calendarYear=None, period=None, currentRatio=None, 
                 quickRatio=None, cashRatio=None, daysOfSalesOutstanding=None, daysOfInventoryOutstanding=None, 
                 operatingCycle=None, daysOfPayablesOutstanding=None, cashConversionCycle=None, grossProfitMargin=None, 
                 operatingProfitMargin=None, pretaxProfitMargin=None, netProfitMargin=None, effectiveTaxRate=None, 
                 returnOnAssets=None, returnOnEquity=None, returnOnCapitalEmployed=None, netIncomePerEBT=None, 
                 ebtPerEbit=None, ebitPerRevenue=None, debtRatio=None, debtEquityRatio=None, 
                 longTermDebtToCapitalization=None, totalDebtToCapitalization=None, interestCoverage=None, 
                 cashFlowToDebtRatio=None, companyEquityMultiplier=None, receivablesTurnover=None, 
                 payablesTurnover=None, inventoryTurnover=None, fixedAssetTurnover=None, assetTurnover=None, 
                 operatingCashFlowPerShare=None, freeCashFlowPerShare=None, cashPerShare=None, payoutRatio=None, 
                 operatingCashFlowSalesRatio=None, freeCashFlowOperatingCashFlowRatio=None, cashFlowCoverageRatios=None, 
                 shortTermCoverageRatios=None, capitalExpenditureCoverageRatio=None, 
                 dividendPaidAndCapexCoverageRatio=None, dividendPayoutRatio=None, priceBookValueRatio=None, 
                 priceToBookRatio=None, priceToSalesRatio=None, priceEarningsRatio=None, priceToFreeCashFlowsRatio=None, 
                 priceToOperatingCashFlowsRatio=None, priceCashFlowRatio=None, priceEarningsToGrowthRatio=None, 
                 priceSalesRatio=None, dividendYield=None, enterpriseValueMultiple=None, priceFairValue=None):
        super().__init__(api_key)
        self.symbol = symbol
        self.date = date
        self.calendarYear = calendarYear
        self.period = period
        self.currentRatio = currentRatio
        self.quickRatio = quickRatio
        self.cashRatio = cashRatio
        self.daysOfSalesOutstanding = daysOfSalesOutstanding
        self.daysOfInventoryOutstanding = daysOfInventoryOutstanding
        self.operatingCycle = operatingCycle
        self.daysOfPayablesOutstanding = daysOfPayablesOutstanding
        self.cashConversionCycle = cashConversionCycle
        self.grossProfitMargin = grossProfitMargin
        self.operatingProfitMargin = operatingProfitMargin
        self.pretaxProfitMargin = pretaxProfitMargin
        self.netProfitMargin = netProfitMargin
        self.effectiveTaxRate = effectiveTaxRate
        self.returnOnAssets = returnOnAssets
        self.returnOnEquity = returnOnEquity
        self.returnOnCapitalEmployed = returnOnCapitalEmployed
        self.netIncomePerEBT = netIncomePerEBT
        self.ebtPerEbit = ebtPerEbit
        self.ebitPerRevenue = ebitPerRevenue
        self.debtRatio = debtRatio
        self.debtEquityRatio = debtEquityRatio
        self.longTermDebtToCapitalization = longTermDebtToCapitalization
        self.totalDebtToCapitalization = totalDebtToCapitalization
        self.interestCoverage = interestCoverage
        self.cashFlowToDebtRatio = cashFlowToDebtRatio
        self.companyEquityMultiplier = companyEquityMultiplier
        self.receivablesTurnover = receivablesTurnover
        self.payablesTurnover = payablesTurnover
        self.inventoryTurnover = inventoryTurnover
        self.fixedAssetTurnover = fixedAssetTurnover
        self.assetTurnover = assetTurnover
        self.operatingCashFlowPerShare = operatingCashFlowPerShare
        self.freeCashFlowPerShare = freeCashFlowPerShare
        self.cashPerShare = cashPerShare
        self.payoutRatio = payoutRatio
        self.operatingCashFlowSalesRatio = operatingCashFlowSalesRatio
        self.freeCashFlowOperatingCashFlowRatio = freeCashFlowOperatingCashFlowRatio
        self.cashFlowCoverageRatios = cashFlowCoverageRatios
        self.shortTermCoverageRatios = shortTermCoverageRatios
        self.capitalExpenditureCoverageRatio = capitalExpenditureCoverageRatio
        self.dividendPaidAndCapexCoverageRatio = dividendPaidAndCapexCoverageRatio
        self.dividendPayoutRatio = dividendPayoutRatio
        self.priceBookValueRatio = priceBookValueRatio
        self.priceToBookRatio = priceToBookRatio
        self.priceToSalesRatio = priceToSalesRatio
        self.priceEarningsRatio = priceEarningsRatio
        self.priceToFreeCashFlowsRatio = priceToFreeCashFlowsRatio
        self.priceToOperatingCashFlowsRatio = priceToOperatingCashFlowsRatio
        self.priceCashFlowRatio = priceCashFlowRatio
        self.priceEarningsToGrowthRatio = priceEarningsToGrowthRatio
        self.priceSalesRatio = priceSalesRatio
        self.dividendYield = dividendYield
        self.enterpriseValueMultiple = enterpriseValueMultiple
        self.priceFairValue = priceFairValue
    def fetch(self, symbol):
        endpoint = f"v3/ratios/{symbol}"
        return self._make_request(endpoint)