// 🧮 ROI 계산 로직
function calculateROI({
  price1, price2, price3,
  subMonthly, subAnnual,
  conversionRate, customerCount, marketingCost
}) {
  const cr = conversionRate / 100; // % → 소수
  const monthlyMarketing = marketingCost;
  const cogs = 0; // 디지털 콘텐츠

  const singleSales = [price1, price2, price3].map(price => ({
    price,
    customers: Math.floor(customerCount * cr),
    revenue: price * Math.floor(customerCount * cr),
    cost: cogs,
    profit: (price - cogs) * Math.floor(customerCount * cr),
    roi: (price - cogs) / price * 100
  }));

  const subSales = {
    monthly: {
      customers: Math.floor(customerCount * cr),
      revenue: subMonthly * Math.floor(customerCount * cr),
      cost: cogs,
      profit: (subMonthly - cogs) * Math.floor(customerCount * cr),
      roi: (subMonthly - cogs) / subMonthly * 100
    },
    annual: {
      customers: Math.floor(customerCount * cr),
      revenue: subAnnual * Math.floor(customerCount * cr),
      cost: cogs,
      profit: (subAnnual - cogs) * Math.floor(customerCount * cr),
      roi: (subAnnual - cogs) / subAnnual * 100
    }
  };

  const totalRevenue = singleSales.reduce((sum, s) => sum + s.revenue, 0) +
                       subSales.monthly.revenue + subSales.annual.revenue;
  const totalProfit = singleSales.reduce((sum, s) => sum + s.profit, 0) +
                      subSales.monthly.profit + subSales.annual.profit;
  const totalCost = monthlyMarketing;
  const netProfit = totalProfit - totalCost;
  const roi = totalCost > 0 ? (netProfit / totalCost) * 100 : 1000;

  return {
    scenarioName: `CR${conversionRate}%_Cust${customerCount}`,
    conversionRate,
    customerCount,
    marketingCost,
    singleSales,
    subSales,
    totalRevenue,
    totalCost,
    netProfit,
    roi
  };
}

// 📥 입력 폼 처리
document.getElementById('roiForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const formData = {
    price1: parseFloat(document.getElementById('price1').value),
    price2: parseFloat(document.getElementById('price2').value),
    price3: parseFloat(document.getElementById('price3').value),
    subMonthly: parseFloat(document.getElementById('subMonthly').value),
    subAnnual: parseFloat(document.getElementById('subAnnual').value),
    conversionRate: parseFloat(document.getElementById('conversionRate').value),
    customerCount: parseInt(document.getElementById('customerCount').value),
    marketingCost: parseFloat(document.getElementById('marketingCost').value)
  };

  const result = calculateROI(formData);
  renderResults(result);
});

// 📊 결과 렌더링
function renderResults(result) {
  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = `
    <div class="result-card">
      <h3>📈 시나리오: ${result.scenarioName}</h3>
      <div class="metric"><span>총 수익</span><strong>${result.totalRevenue.toLocaleString()} 원</strong></div>
      <div class="metric"><span>총 비용</span><strong>${result.totalCost.toLocaleString()} 원</strong></div>
      <div class="metric"><span>순이익</span><strong>${result.netProfit.toLocaleString()} 원</strong></div>
      <div class="metric"><span>ROI</span><strong>${result.roi.toFixed(2)} %</strong></div>
    </div>
    <div class="result-card">
      <h4>单品별 이익</h4>
      ${result.singleSales.map(s => `
        <div class="metric"><span>${s.price.toLocaleString()} 원 (고객 ${s.customers}명)</span><strong>${s.profit.toLocaleString()} 원</strong></div>
      `).join('')}
    </div>
    <div class="result-card">
      <h4>구독 이익</h4>
      <div class="metric"><span>월 구독 (${result.subSales.monthly.customers}명)</span><strong>${result.subSales.monthly.profit.toLocaleString()} 원</strong></div>
      <div class="metric"><span>연번들 (${result.subSales.annual.customers}명)</span><strong>${result.subSales.annual.profit.toLocaleString()} 원</strong></div>
    </div>
  `;
}

// 💾 저장/로드
document.getElementById('saveBtn').addEventListener('click', () => {
  const formData = {
    price1: parseFloat(document.getElementById('price1').value),
    price2: parseFloat(document.getElementById('price2').value),
    price3: parseFloat(document.getElementById('price3').value),
    subMonthly: parseFloat(document.getElementById('subMonthly').value),
    subAnnual: parseFloat(document.getElementById('subAnnual').value),
    conversionRate: parseFloat(document.getElementById('conversionRate').value),
    customerCount: parseInt(document.getElementById('customerCount').value),
    marketingCost: parseFloat(document.getElementById('marketingCost').value)
  };
  const result = calculateROI(formData);

  db.ref('scenarios/' + result.scenarioName).set(result)
    .then(() => alert(`✅ 저장 완료: ${result.scenarioName}`))
    .catch(err => alert(`❌ 저장 실패: ${err.message}`));
});

document.getElementById('loadBtn').addEventListener('click', () => {
  db.ref('scenarios/').on('value', (snapshot) => {
    const scenarios = snapshot.val();
    const select = document.getElementById('scenarioSelect');
    select.innerHTML = '<option value="">선택하세요…</option>';
    Object.keys(scenarios || {}).forEach(key => {
      const opt = document.createElement('option');
      opt.value = key;
      opt.textContent = `${key} (CR${scenarios[key].conversionRate}%, 고객 ${scenarios[key].customerCount}명)`;
      select.appendChild(opt);
    });
    select.style.display = 'block';
  });
});

// 📋 시나리오 로드 시 결과 자동 렌더링
document.getElementById('scenarioSelect').addEventListener('change', (e) => {
  const name = e.target.value;
  if (!name) return;
  db.ref('scenarios/' + name).on('value', (snapshot) => {
    const scenario = snapshot.val();
    renderResults(scenario);
  });
});