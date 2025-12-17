import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide03Conservative: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-12 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-emerald-400 mb-8">Strategia Conservativa</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-8">
        {/* Left Column - Details */}
        <div className="flex flex-col gap-4">
          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-6">
            <h3 className="text-2xl font-semibold text-emerald-300 mb-3">🎯 Obiettivo</h3>
            <p className="text-slate-200 text-lg">
              Crescita stabile del capitale con rischio controllato attraverso vendita di Put OTM (Out-of-The-Money) su S&P 500.
            </p>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
            <h4 className="text-xl font-semibold text-white mb-3">Parametri Chiave</h4>
            <div className="space-y-2 text-slate-300">
              <div className="flex justify-between">
                <span>Delta Target:</span>
                <span className="text-emerald-400 font-semibold">-0.05 a -0.10</span>
              </div>
              <div className="flex justify-between">
                <span>Strike Method:</span>
                <span className="text-emerald-400 font-semibold">Delta-VIX o Tabella</span>
              </div>
              <div className="flex justify-between">
                <span>DTE (Days to Expiry):</span>
                <span className="text-emerald-400 font-semibold">23-35 giorni</span>
              </div>
              <div className="flex justify-between">
                <span>Margine Utilizzato:</span>
                <span className="text-emerald-400 font-semibold">Configurabile</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
            <h4 className="text-xl font-semibold text-white mb-3">🛡️ Protezioni</h4>
            <ul className="space-y-2 text-slate-300">
              <li className="flex items-start gap-2">
                <span className="text-blue-400">•</span>
                <span>Buy Put automatico su spike VIX</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-blue-400">•</span>
                <span>KO sintetico per protezione estrema</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-blue-400">•</span>
                <span>Alert margine a 2 soglie (50%, 75%)</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Right Column - Image */}
        <div className="flex flex-col gap-4 min-h-0">
          <div className="flex-1 min-h-0 bg-slate-800/30 border border-emerald-500/30 rounded-xl overflow-hidden">
            <img 
              src="/assets/strategy-conservative-chart.jpg" 
              alt="Conservative Strategy Chart" 
              className="w-full h-full object-cover"
            />
          </div>
          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-4">
            <p className="text-emerald-300 text-center font-semibold text-lg">
              ✅ Rischio Basso • Rendimento Stabile • Protezione Automatica
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Strategia Conservativa",
  order: 2,
})(Slide03Conservative);

export default Slide03Conservative;