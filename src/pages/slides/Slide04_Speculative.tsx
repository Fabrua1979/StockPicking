import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide04SemiConservative: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-amber-400 mb-6">Strategia Semi-Conservativa</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-8">
        {/* Left Column - Details */}
        <div className="flex flex-col gap-3">
          <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-5">
            <h3 className="text-2xl font-semibold text-amber-300 mb-2">⚡ Obiettivo</h3>
            <p className="text-slate-200 text-base">
              Rendimenti maggiori con rischio controllato attraverso vendita di Put con strike più vicini al prezzo corrente (delta -0.01 a -0.08).
            </p>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h4 className="text-xl font-semibold text-white mb-2">Parametri Chiave</h4>
            <div className="space-y-2 text-slate-300 text-sm">
              <div className="flex justify-between">
                <span>Delta Target:</span>
                <span className="text-amber-400 font-semibold">-0.01 a -0.08</span>
              </div>
              <div className="flex justify-between">
                <span>Strike Method:</span>
                <span className="text-amber-400 font-semibold">Delta-VIX o Tabella</span>
              </div>
              <div className="flex justify-between">
                <span>DTE (Days to Expiry):</span>
                <span className="text-amber-400 font-semibold">23-35 giorni</span>
              </div>
              <div className="flex justify-between">
                <span>Rischio:</span>
                <span className="text-amber-400 font-semibold">Medio-Alto</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h4 className="text-xl font-semibold text-white mb-2">⚡ Caratteristiche</h4>
            <ul className="space-y-1 text-slate-300 text-sm">
              <li className="flex items-start gap-2">
                <span className="text-amber-400">•</span>
                <span>Strike più vicini al prezzo spot</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-amber-400">•</span>
                <span>Premi più elevati per contratto</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-amber-400">•</span>
                <span>Sistema di alert e rifinanziamento</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-amber-400">•</span>
                <span>Coperture opzionali su spike VIX</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Right Column - Image */}
        <div className="flex flex-col gap-4 min-h-0">
          <div className="flex-1 min-h-0 bg-slate-800/30 border border-amber-500/30 rounded-xl overflow-hidden">
            <img 
              src="/assets/strategy-speculative-chart.jpg" 
              alt="Semi-Conservative Strategy Chart" 
              className="w-full h-full object-cover"
            />
          </div>
          <div className="bg-amber-500/10 border border-amber-500/30 rounded-lg p-4">
            <p className="text-amber-300 text-center font-semibold text-lg">
              ⚖️ Rischio Medio-Alto • Rendimento Elevato • Gestione Attiva
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Strategia Semi-Conservativa",
  order: 3,
})(Slide04SemiConservative);

export default Slide04SemiConservative;