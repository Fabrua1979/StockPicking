import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide06Parameters: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-4xl font-bold text-indigo-400 mb-6">Parametri Principali</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-6">
        {/* Left Column - Capital and Margin */}
        <div className="flex flex-col gap-4">
          <div className="bg-indigo-500/10 border border-indigo-500/30 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-indigo-300 mb-3">💰 Gestione Capitale</h3>
            <div className="space-y-2 text-slate-300 text-sm">
              <div className="flex justify-between items-center">
                <span>Capitale Iniziale Conservativa:</span>
                <span className="text-emerald-400 font-semibold">Configurabile</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Capitale Iniziale Semi-C:</span>
                <span className="text-amber-400 font-semibold">Configurabile</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Capitale Iniziale SCV:</span>
                <span className="text-violet-400 font-semibold">Opzionale</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-white mb-3">📊 Margine e Alert</h3>
            <div className="space-y-2 text-slate-300 text-sm">
              <div className="flex justify-between items-center">
                <span>Soglia Alert S1:</span>
                <span className="text-yellow-400 font-semibold">50%</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Soglia Alert S2:</span>
                <span className="text-red-400 font-semibold">75%</span>
              </div>
              <div className="flex justify-between items-center">
                <span>% Margine:</span>
                <span className="text-blue-400 font-semibold">Varia per broker</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Rifinanziamento:</span>
                <span className="text-emerald-400 font-semibold">20-50%</span>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column - DTE and Profiles */}
        <div className="flex flex-col gap-4">
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-white mb-3">📅 DTE (Days to Expiry)</h3>
            <div className="space-y-2 text-slate-300 text-sm">
              <div className="flex justify-between items-center">
                <span>DTE Minimo:</span>
                <span className="text-blue-400 font-semibold">23 giorni</span>
              </div>
              <div className="flex justify-between items-center">
                <span>DTE Massimo:</span>
                <span className="text-blue-400 font-semibold">35 giorni</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Logica Scadenza:</span>
                <span className="text-blue-400 font-semibold">Broker-specific</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-white mb-3">🎯 Profili di Ingresso</h3>
            <div className="space-y-2 text-slate-300 text-xs">
              <div className="bg-slate-700/50 rounded-lg p-2">
                <div className="text-blue-400 font-semibold text-sm">Profilo 1: RSI/MACD</div>
                <div className="text-slate-400 text-xs">Segnali tecnici con conferma</div>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-2">
                <div className="text-purple-400 font-semibold text-sm">Profilo 2: ICP</div>
                <div className="text-slate-400 text-xs">Indicatore composito 7+ fattori</div>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-2">
                <div className="text-cyan-400 font-semibold text-sm">Profilo 3: ICP + Conferma</div>
                <div className="text-slate-400 text-xs">ICP con attesa candela rossa</div>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-2">
                <div className="text-emerald-400 font-semibold text-sm">Profilo 4: Probabilità/EMA</div>
                <div className="text-slate-400 text-xs">SD implicita da VIX e EMA 100</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Parametri Principali",
  order: 9,
})(Slide06Parameters);

export default Slide06Parameters;