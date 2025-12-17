import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide07ChartSymbols: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-8 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-4xl font-bold text-purple-400 mb-4">Simboli sul Grafico</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-4">
        {/* Left Column - Entry Symbols */}
        <div className="flex flex-col gap-2 min-h-0">
          <div className="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
            <h3 className="text-lg font-semibold text-purple-300 mb-2">🎯 Simboli Ingresso</h3>
            <div className="space-y-1">
              <div className="flex items-center gap-2 bg-slate-800/50 rounded p-1">
                <span className="text-xl">🟢</span>
                <div>
                  <div className="text-emerald-400 font-semibold text-xs">Conservativa</div>
                  <div className="text-slate-400 text-xs">Delta -0.05/-0.10</div>
                </div>
              </div>
              <div className="flex items-center gap-2 bg-slate-800/50 rounded p-1">
                <span className="text-xl">🟡</span>
                <div>
                  <div className="text-amber-400 font-semibold text-xs">Semi-Conservativa</div>
                  <div className="text-slate-400 text-xs">Delta -0.01/-0.08</div>
                </div>
              </div>
              <div className="flex items-center gap-2 bg-slate-800/50 rounded p-1">
                <span className="text-xl">🟣</span>
                <div>
                  <div className="text-violet-400 font-semibold text-xs">SCV (Opzionale)</div>
                  <div className="text-slate-400 text-xs">Call su VIX</div>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-lg font-semibold text-white mb-2">✅ Simboli Uscita</h3>
            <div className="space-y-1">
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-xl">✔️</span>
                <div className="text-emerald-400 font-semibold text-xs">Uscita Profitto</div>
              </div>
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-xl">❌</span>
                <div className="text-red-400 font-semibold text-xs">Uscita Perdita</div>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-lg font-semibold text-white mb-2">🛡️ Coperture</h3>
            <div className="space-y-1">
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-xl">🔵</span>
                <div className="text-blue-400 font-semibold text-xs">Buy Put Protettiva</div>
              </div>
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-xl">🔶</span>
                <div className="text-orange-400 font-semibold text-xs">KO Sintetico</div>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column - Alerts and Image */}
        <div className="flex flex-col gap-2 min-h-0">
          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-lg font-semibold text-white mb-2">⚠️ Alert</h3>
            <div className="space-y-1">
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-lg">⚠️</span>
                <div className="text-yellow-400 font-semibold text-xs">S1 (50%)</div>
              </div>
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-lg">🚨</span>
                <div className="text-red-400 font-semibold text-xs">S2 (75%)</div>
              </div>
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-lg">💰</span>
                <div className="text-emerald-400 font-semibold text-xs">Rifinanziamento</div>
              </div>
              <div className="flex items-center gap-2 bg-slate-700/50 rounded p-1">
                <span className="text-lg">💸</span>
                <div className="text-cyan-400 font-semibold text-xs">Prelievo</div>
              </div>
            </div>
          </div>

          <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-2">
            <h3 className="text-sm font-semibold text-blue-300 mb-1">📊 Linee Strike</h3>
            <div className="space-y-1 text-xs text-slate-300">
              <div className="flex items-center gap-2">
                <div className="w-6 h-0.5 bg-emerald-500"></div>
                <span>Conservativa</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-6 h-0.5 bg-amber-500"></div>
                <span>Semi-Conservativa</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-6 h-0.5 bg-violet-500"></div>
                <span>SCV (Call VIX)</span>
              </div>
            </div>
          </div>

          <div className="flex-1 min-h-0 bg-slate-800/30 border border-purple-500/30 rounded-lg overflow-hidden p-2">
            <img 
              src="/assets/DettagliosimbolientrataLineaStrike.png" 
              alt="Chart Symbols" 
              className="w-full h-full object-contain"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Simboli sul Grafico",
  order: 6,
})(Slide07ChartSymbols);

export default Slide07ChartSymbols;