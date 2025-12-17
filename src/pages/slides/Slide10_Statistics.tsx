import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";
import { Chart } from "@/components/ui/chart";

const Slide10Statistics: React.FC = () => {
  // Sample data for performance chart
  const performanceData = [
    { month: "Gen", conservativa: 2.5, speculativa: 4.2, scv: 3.1 },
    { month: "Feb", conservativa: 3.1, speculativa: 5.8, scv: 2.8 },
    { month: "Mar", conservativa: 2.8, speculativa: -2.1, scv: 4.5 },
    { month: "Apr", conservativa: 3.5, speculativa: 6.2, scv: 3.8 },
    { month: "Mag", conservativa: 2.9, speculativa: 4.5, scv: -1.2 },
    { month: "Giu", conservativa: 3.2, speculativa: 7.1, scv: 5.2 },
  ];

  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-emerald-400 mb-6">Statistiche e Performance</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-8">
        {/* Left Column - Chart */}
        <div className="flex flex-col gap-4 min-h-0">
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-5 flex-1 min-h-0">
            <h3 className="text-xl font-semibold text-white mb-4">📊 Performance Mensile (%)</h3>
            <Chart
              type="bar"
              data={performanceData}
              series={["conservativa", "speculativa", "scv"]}
              xKey="month"
              colors={["#10B981", "#F59E0B", "#8B5CF6"]}
              height={280}
            />
          </div>
        </div>

        {/* Right Column - Stats Cards */}
        <div className="flex flex-col gap-3">
          <div className="grid grid-cols-2 gap-3">
            <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-3">
              <div className="text-emerald-400 text-xs mb-1">Success Rate C1</div>
              <div className="text-white text-2xl font-bold">87.5%</div>
              <div className="text-slate-400 text-xs mt-1">35/40 trades</div>
            </div>
            <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-3">
              <div className="text-amber-400 text-xs mb-1">Success Rate Spec</div>
              <div className="text-white text-2xl font-bold">72.3%</div>
              <div className="text-slate-400 text-xs mt-1">29/40 trades</div>
            </div>
            <div className="bg-violet-500/10 border border-violet-500/30 rounded-xl p-3">
              <div className="text-violet-400 text-xs mb-1">Success Rate SCV</div>
              <div className="text-white text-2xl font-bold">81.2%</div>
              <div className="text-slate-400 text-xs mt-1">13/16 trades</div>
            </div>
            <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-3">
              <div className="text-blue-400 text-xs mb-1">P/L Aggregato</div>
              <div className="text-emerald-400 text-2xl font-bold">+$18.2K</div>
              <div className="text-slate-400 text-xs mt-1">+12.1% ROI</div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-white mb-2">📈 Metriche Chiave</h3>
            <div className="space-y-2 text-xs">
              <div className="flex justify-between items-center">
                <span className="text-slate-400">Operazioni Coperte:</span>
                <span className="text-cyan-400 font-semibold">12 (12.5%)</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-slate-400">Alert Margine S1:</span>
                <span className="text-yellow-400 font-semibold">8 eventi</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-slate-400">Alert Margine S2:</span>
                <span className="text-red-400 font-semibold">3 eventi</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-slate-400">Rifinanziamenti:</span>
                <span className="text-blue-400 font-semibold">$15,000</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-slate-400">Prelievi Totali:</span>
                <span className="text-emerald-400 font-semibold">$8,500</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-white mb-2">💡 Insights</h3>
            <ul className="space-y-1 text-slate-300 text-xs">
              <li className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span>Conservativa: stabilità eccellente</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-amber-400">✓</span>
                <span>Speculativa: volatilità controllata</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-violet-400">✓</span>
                <span>SCV: timing ingresso ottimale</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Statistiche e Performance",
  order: 9,
})(Slide10Statistics);

export default Slide10Statistics;