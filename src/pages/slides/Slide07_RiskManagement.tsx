import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide07RiskManagement: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-blue-400 mb-6">Gestione del Rischio</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-8">
        {/* Left Column - Risk Features */}
        <div className="flex flex-col gap-3">
          <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-blue-300 mb-2">📈 Margine Dinamico</h3>
            <p className="text-slate-300 text-sm mb-2">
              Calcolo real-time dell'occupazione del margine basato su:
            </p>
            <ul className="space-y-1 text-slate-300 text-xs">
              <li className="flex items-start gap-2">
                <span className="text-blue-400">•</span>
                <span>Prezzo corrente dell'opzione venduta</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-blue-400">•</span>
                <span>Valore coperture attive (Buy Put o KO)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-blue-400">•</span>
                <span>Margine broker dinamico per profilo</span>
              </li>
            </ul>
          </div>

          <div className="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-yellow-300 mb-2">🚨 Sistema Alert 2 Soglie</h3>
            <div className="space-y-2">
              <div className="bg-slate-800/50 rounded-lg p-2">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-yellow-400 text-lg">⚠️</span>
                  <span className="text-yellow-300 font-semibold text-sm">Soglia 1 (50%)</span>
                </div>
                <p className="text-slate-400 text-xs">Alert visivo, nessuna azione automatica</p>
              </div>
              <div className="bg-slate-800/50 rounded-lg p-2">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-red-400 text-lg">🚨</span>
                  <span className="text-red-300 font-semibold text-sm">Soglia 2 (75%)</span>
                </div>
                <p className="text-slate-400 text-xs">Rifinanziamento automatico o chiusura posizione</p>
              </div>
            </div>
          </div>

          <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
            <h3 className="text-xl font-semibold text-red-300 mb-2">🦢 Copertura Cigno Nero</h3>
            <p className="text-slate-300 text-xs mb-2">
              Attivazione automatica quando VIX supera soglia configurabile (es. 30). Opzioni:
            </p>
            <div className="space-y-1 text-slate-400 text-xs">
              <div>• Buy Put protettiva</div>
              <div>• KO sintetico (short S&P 500)</div>
              <div>• Chiusura immediata posizione</div>
            </div>
          </div>
        </div>

        {/* Right Column - Image and Summary */}
        <div className="flex flex-col gap-4 min-h-0">
          <div className="flex-1 min-h-0 bg-slate-800/30 border border-blue-500/30 rounded-xl overflow-hidden">
            <img 
              src="/assets/risk-management-shield.jpg" 
              alt="Risk Management" 
              className="w-full h-full object-cover"
            />
          </div>
          
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-white mb-2">✅ Vantaggi Chiave</h3>
            <ul className="space-y-1 text-slate-300 text-xs">
              <li className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span>Protezione automatica su eventi estremi</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span>Monitoraggio continuo 24/7</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span>Decisioni basate su dati real-time</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span>Riduzione rischio catastrofico</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Gestione del Rischio",
  order: 10,
})(Slide07RiskManagement);

export default Slide07RiskManagement;