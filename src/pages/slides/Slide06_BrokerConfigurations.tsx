import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide06BrokerConfigurations: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-8 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-4xl font-bold text-blue-400 mb-4">Configurazioni Broker Ottimizzate</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-4">
        {/* Left Column - Broker Configs */}
        <div className="flex flex-col gap-2 min-h-0 overflow-y-auto">
          <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
            <h3 className="text-base font-semibold text-blue-300 mb-2">🏦 AVA Trade</h3>
            <div className="space-y-1 text-xs text-slate-300">
              <div className="flex justify-between">
                <span>Premio in Margine:</span>
                <span className="text-blue-400 font-semibold">Sì</span>
              </div>
              <div className="flex justify-between">
                <span>Scadenza:</span>
                <span className="text-blue-400 font-semibold">Durata Fissa</span>
              </div>
              <div className="flex justify-between">
                <span>Delta C/Semi-C:</span>
                <span className="text-emerald-400 font-semibold">-0.05/-0.05</span>
              </div>
              <div className="flex justify-between">
                <span>Margine %:</span>
                <span className="text-white font-semibold">52%/58%</span>
              </div>
              <div className="flex justify-between">
                <span>Rifin./Molt.:</span>
                <span className="text-white font-semibold">20%/1</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-white mb-2">🏦 IG Italia</h3>
            <div className="space-y-1 text-xs text-slate-300">
              <div className="flex justify-between">
                <span>Premio in Margine:</span>
                <span className="text-red-400 font-semibold">No</span>
              </div>
              <div className="flex justify-between">
                <span>Scadenza:</span>
                <span className="text-blue-400 font-semibold">Mensili 3° Ven</span>
              </div>
              <div className="flex justify-between">
                <span>Delta C/Semi-C:</span>
                <span className="text-emerald-400 font-semibold">-0.05/-0.08</span>
              </div>
              <div className="flex justify-between">
                <span>Margine %:</span>
                <span className="text-white font-semibold">57%/45%</span>
              </div>
              <div className="flex justify-between">
                <span>Rifin./Molt.:</span>
                <span className="text-white font-semibold">20%/1</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-white mb-2">🏦 IG UK/Intl/Aus</h3>
            <div className="space-y-1 text-xs text-slate-300">
              <div className="flex justify-between">
                <span>Margine %:</span>
                <span className="text-white font-semibold">51%/45%</span>
              </div>
              <div className="flex justify-between">
                <span>Moltiplicatore:</span>
                <span className="text-cyan-400 font-semibold">100</span>
              </div>
              <div className="text-slate-400 text-xs">Altri come IG Italia</div>
            </div>
          </div>
        </div>

        {/* Right Column - More Brokers */}
        <div className="flex flex-col gap-2 min-h-0">
          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-3">
            <h3 className="text-base font-semibold text-white mb-2">🏦 IG Europa</h3>
            <div className="space-y-1 text-xs text-slate-300">
              <div className="flex justify-between">
                <span>Premio in Margine:</span>
                <span className="text-red-400 font-semibold">No</span>
              </div>
              <div className="flex justify-between">
                <span>Scadenza:</span>
                <span className="text-blue-400 font-semibold">Mensili 3° Ven</span>
              </div>
              <div className="flex justify-between">
                <span>Delta C/Semi-C:</span>
                <span className="text-emerald-400 font-semibold">-0.05/-0.08</span>
              </div>
              <div className="flex justify-between">
                <span>Margine %:</span>
                <span className="text-emerald-400 font-semibold">27%/22% ⭐</span>
              </div>
              <div className="flex justify-between">
                <span>Rifin./Molt.:</span>
                <span className="text-white font-semibold">20%/1</span>
              </div>
            </div>
          </div>

          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-3">
            <h3 className="text-base font-semibold text-emerald-300 mb-2">🏦 IG Svizzera 🏆</h3>
            <div className="space-y-1 text-xs text-slate-300">
              <div className="flex justify-between">
                <span>Premio in Margine:</span>
                <span className="text-red-400 font-semibold">No</span>
              </div>
              <div className="flex justify-between">
                <span>Scadenza:</span>
                <span className="text-blue-400 font-semibold">Mensili 3° Ven</span>
              </div>
              <div className="flex justify-between">
                <span>Delta C/Semi-C:</span>
                <span className="text-emerald-400 font-semibold">-0.05/-0.05</span>
              </div>
              <div className="flex justify-between">
                <span>Margine %:</span>
                <span className="text-emerald-400 font-bold">10%/10% 🏆</span>
              </div>
              <div className="flex justify-between">
                <span>Rifin./Molt.:</span>
                <span className="text-emerald-400 font-bold">50%/100 🏆</span>
              </div>
            </div>
          </div>

          <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-2">
            <p className="text-blue-300 text-center font-semibold text-xs">
              💡 Configurazione automatica per broker
            </p>
          </div>

          <div className="flex-1 min-h-0 bg-slate-800/50 border border-slate-700 rounded-lg p-2">
            <h4 className="text-white font-semibold text-xs mb-2">📊 Pannelli Impostazioni</h4>
            <div className="grid grid-cols-2 gap-2">
              <img src="/assets/ImpostazioniPannello1.png" alt="Panel 1" className="w-full rounded border border-slate-600" />
              <img src="/assets/Impostazionipannello2.png" alt="Panel 2" className="w-full rounded border border-slate-600" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Configurazioni Broker",
  order: 5,
})(Slide06BrokerConfigurations);

export default Slide06BrokerConfigurations;