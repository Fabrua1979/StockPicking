import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide08EntrySignals: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-emerald-400 mb-6">Segnali di Ingresso</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-6">
        {/* Left Column - Signal Methods */}
        <div className="flex flex-col gap-3">
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-blue-300 mb-2">📊 RSI/MACD Classico</h3>
            <p className="text-slate-300 text-xs mb-2">Segnali tecnici tradizionali:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• Conservativa: RSI &gt; RSI-SMA e MACD &gt; Signal</li>
              <li>• Semi-Conservativa: MACD &gt; Signal e MACD &lt; 0</li>
              <li>• Attesa candela rossa per conferma</li>
            </ul>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-violet-300 mb-2">🎯 ICP (Indicatore Composito)</h3>
            <p className="text-slate-300 text-xs mb-2">Indicatore proprietario multi-fattore:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• Combina RSI, MACD, MA30, MA200</li>
              <li>• Momentum, Stochastic, Pivot Points</li>
              <li>• Volume analysis pesato</li>
            </ul>
          </div>

          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-emerald-300 mb-2">⭐ Profilo 4: Probabilità/EMA</h3>
            <p className="text-slate-300 text-xs mb-2">Approccio innovativo basato su probabilità:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• Calcolo SD giornaliera implicita da VIX</li>
              <li>• Probabilità di estensione ribassista</li>
              <li>• Confronto con EMA 100</li>
            </ul>
          </div>
        </div>

        {/* Right Column - Details and Filters */}
        <div className="flex flex-col gap-3">
          <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-blue-300 mb-2">🔍 Filtri Aggiuntivi</h3>
            <div className="space-y-2">
              <div className="bg-slate-800/50 rounded-lg p-2">
                <div className="text-white font-semibold text-xs mb-1">Volatilità</div>
                <p className="text-slate-400 text-xs">VIX, VXV, SKEW per contesto di mercato</p>
              </div>
              <div className="bg-slate-800/50 rounded-lg p-2">
                <div className="text-white font-semibold text-xs mb-1">Cigno Nero</div>
                <p className="text-slate-400 text-xs">Blocco ingressi se VIX &gt; soglia critica</p>
              </div>
              <div className="bg-slate-800/50 rounded-lg p-2">
                <div className="text-white font-semibold text-xs mb-1">Timeframe</div>
                <p className="text-slate-400 text-xs">Analisi su TF configurabile (default: Chart)</p>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-white mb-2">⏱️ Logica di Attesa</h3>
            <p className="text-slate-300 text-xs mb-2">
              Sistema intelligente di conferma segnale:
            </p>
            <div className="space-y-1">
              <div className="flex items-start gap-2 text-slate-400 text-xs">
                <span className="text-emerald-400">1.</span>
                <span>Segnale trigger (RSI/MACD o ICP)</span>
              </div>
              <div className="flex items-start gap-2 text-slate-400 text-xs">
                <span className="text-emerald-400">2.</span>
                <span>Attesa candela rossa entro 5 barre</span>
              </div>
              <div className="flex items-start gap-2 text-slate-400 text-xs">
                <span className="text-emerald-400">3.</span>
                <span>Ingresso immediato o scarto segnale</span>
              </div>
            </div>
          </div>

          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-3">
            <p className="text-emerald-300 text-center font-semibold text-xs">
              ✨ Profilo 4 bypassa l'attesa: ingresso immediato su probabilità favorevole
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Segnali di Ingresso",
  order: 11,
})(Slide08EntrySignals);

export default Slide08EntrySignals;