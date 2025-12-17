import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide05SCV: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-violet-400 mb-6">Strategia SCV (Opzionale)</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-8">
        {/* Left Column - Details */}
        <div className="flex flex-col gap-3">
          <div className="bg-violet-500/10 border border-violet-500/30 rounded-xl p-5">
            <h3 className="text-2xl font-semibold text-violet-300 mb-2">📉 Obiettivo</h3>
            <p className="text-slate-200 text-base">
              Profitto dalla discesa della volatilità attraverso vendita di Call su VIX dopo spike improvvisi. <span className="text-violet-400 font-semibold">Strategia opzionale attivabile dall'utente.</span>
            </p>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h4 className="text-xl font-semibold text-white mb-2">Parametri Chiave</h4>
            <div className="space-y-2 text-slate-300 text-sm">
              <div className="flex justify-between">
                <span>Underlying:</span>
                <span className="text-violet-400 font-semibold">VIX (TVC:VIX)</span>
              </div>
              <div className="flex justify-between">
                <span>Strike Distance:</span>
                <span className="text-violet-400 font-semibold">+5% sopra VIX</span>
              </div>
              <div className="flex justify-between">
                <span>Scadenza:</span>
                <span className="text-violet-400 font-semibold">3° Mercoledì mese</span>
              </div>
              <div className="flex justify-between">
                <span>DTE Minimo:</span>
                <span className="text-violet-400 font-semibold">23 giorni</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h4 className="text-xl font-semibold text-white mb-2">🎲 Profili di Ingresso</h4>
            <ul className="space-y-1 text-slate-300 text-sm">
              <li className="flex items-start gap-2">
                <span className="text-violet-400">1.</span>
                <span>Spike Detector 1 (VVIX &gt; 120)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-violet-400">2.</span>
                <span>Spike Detector 2 (Bollinger 0.5x)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-violet-400">3.</span>
                <span>Spike Detector 3 (Bollinger + VVIX)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-violet-400">4.</span>
                <span>Crossover Soglia (VIX &gt; 20)</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Right Column - Image */}
        <div className="flex flex-col gap-4 min-h-0">
          <div className="flex-1 min-h-0 bg-slate-800/30 border border-violet-500/30 rounded-xl overflow-hidden">
            <img 
              src="/assets/strategy-scv-volatility.jpg" 
              alt="SCV Volatility Chart" 
              className="w-full h-full object-cover"
            />
          </div>
          <div className="bg-violet-500/10 border border-violet-500/30 rounded-lg p-4">
            <p className="text-violet-300 text-center font-semibold text-lg">
              🌊 Volatility Trading • Opzionale • Nessuna Copertura • Gestione Margine Pura
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Strategia SCV (Opzionale)",
  order: 4,
})(Slide05SCV);

export default Slide05SCV;