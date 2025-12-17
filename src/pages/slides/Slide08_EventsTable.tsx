import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide08EventsTable: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-8 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-4xl font-bold text-cyan-400 mb-4">Eventi Tabella (Basso Sinistra)</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-4">
        {/* Left Column - Event Types */}
        <div className="flex flex-col gap-2 min-h-0">
          <div className="bg-cyan-500/10 border border-cyan-500/30 rounded-lg p-3">
            <h3 className="text-lg font-semibold text-cyan-300 mb-2">📋 Tipi di Eventi</h3>
            <p className="text-slate-300 text-xs">
              Eventi istantanei durante l'esecuzione della strategia
            </p>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-emerald-300 mb-2">🟢 Apertura</h3>
            <div className="space-y-1 text-xs">
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-emerald-400 font-semibold">OPEN CONS</div>
                <div className="text-slate-400 text-xs">Conservativa - Strike, contratti, premio</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-amber-400 font-semibold">OPEN SEMI-C</div>
                <div className="text-slate-400 text-xs">Semi-Conservativa - Strike, contratti</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-violet-400 font-semibold">OPEN SCV</div>
                <div className="text-slate-400 text-xs">SCV (se abilitata) - Call VIX</div>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-blue-300 mb-2">✅ Chiusura</h3>
            <div className="space-y-1 text-xs">
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-emerald-400 font-semibold">CLOSE PROFIT</div>
                <div className="text-slate-400 text-xs">P/L realizzato, % guadagno</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-red-400 font-semibold">CLOSE LOSS</div>
                <div className="text-slate-400 text-xs">Motivo (S2, KO), importo perso</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-blue-400 font-semibold">CLOSE EXPIRY</div>
                <div className="text-slate-400 text-xs">Scadenza OTM, premio trattenuto</div>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column - More Events and Image */}
        <div className="flex flex-col gap-2 min-h-0">
          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-yellow-300 mb-2">⚠️ Alert</h3>
            <div className="space-y-1 text-xs">
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-yellow-400 font-semibold">ALERT S1 (50%)</div>
                <div className="text-slate-400 text-xs">Margine 50% - Solo notifica</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-red-400 font-semibold">ALERT S2 (75%)</div>
                <div className="text-slate-400 text-xs">Margine 75% - Azione richiesta</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-emerald-400 font-semibold">REFINANCE</div>
                <div className="text-slate-400 text-xs">Rifinanziamento, nuovo capitale</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-cyan-400 font-semibold">WITHDRAW</div>
                <div className="text-slate-400 text-xs">Prelievo, capitale residuo</div>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-purple-300 mb-2">🛡️ Coperture</h3>
            <div className="space-y-1 text-xs">
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-blue-400 font-semibold">HEDGE BUY PUT</div>
                <div className="text-slate-400 text-xs">Buy Put - Strike, costo, VIX</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-orange-400 font-semibold">HEDGE KO</div>
                <div className="text-slate-400 text-xs">Short S&P 500, quantità</div>
              </div>
              <div className="bg-slate-700/50 rounded p-1">
                <div className="text-purple-400 font-semibold">HEDGE CLOSE</div>
                <div className="text-slate-400 text-xs">P/L copertura, VIX normalizzato</div>
              </div>
            </div>
          </div>

          <div className="flex-1 min-h-0 bg-slate-800/30 border border-cyan-500/30 rounded-lg overflow-hidden p-2">
            <img 
              src="/assets/Eventibassoasx.png" 
              alt="Events Table" 
              className="w-full h-full object-contain"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Eventi Tabella",
  order: 7,
})(Slide08EventsTable);

export default Slide08EventsTable;