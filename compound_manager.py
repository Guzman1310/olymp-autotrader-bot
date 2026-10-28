"""
Motor de Gestión de Capital con Interés Compuesto (Soros 4 Niveles).
Calcula matemáticamente los importes de cada operación en base al rendimiento (85%).
"""
from config import INITIAL_STAKE, MAX_COMPOUND_CYCLES, PAYOUT_RATE

class CompoundManager:
    def __init__(self):
        self.initial_stake = INITIAL_STAKE
        self.max_cycles = MAX_COMPOUND_CYCLES
        self.payout_rate = PAYOUT_RATE
        self.current_level = 1
        self.current_stake = self.initial_stake
        self.consecutive_wins = 0

    def get_current_stake(self) -> float:
        """Retorna el importe exacto para la siguiente operación."""
        return round(self.current_stake, 2)

    def register_result(self, is_win: bool) -> dict:
        """
        Registra si la operación fue ganada o perdida y calcula el siguiente importe.
        Retorna resumen del ciclo.
        """
        if is_win:
            profit = self.current_stake * self.payout_rate
            self.consecutive_wins += 1
            print(f"[COMPOUND] Ganada nivel {self.current_level}! Beneficio: +${profit:.2f}")

            if self.consecutive_wins >= self.max_cycles:
                # Meta de 4 niveles alcanzada con éxito!
                print(f"[COMPOUND] ¡CICLO DE 4 NIVELES COMPLETADO! Reiniciando a ${self.initial_stake}...")
                completed_cycle = True
                self.current_level = 1
                self.current_stake = self.initial_stake
                self.consecutive_wins = 0
            else:
                # Sumar capital + ganancia para la siguiente operación
                completed_cycle = False
                self.current_level += 1
                self.current_stake = round(self.current_stake + profit, 2)
                
            return {
                "win": True,
                "profit": profit,
                "next_level": self.current_level,
                "next_stake": self.current_stake,
                "cycle_completed": completed_cycle
            }
        else:
            # En caso de pérdida, reinicio inmediato al nivel 1 ($10 USD)
            print(f"[COMPOUND] Pérdida en nivel {self.current_level}. Reiniciando a ${self.initial_stake}...")
            loss_amount = self.current_stake
            self.current_level = 1
            self.current_stake = self.initial_stake
            self.consecutive_wins = 0
            return {
                "win": False,
                "profit": -loss_amount,
                "next_level": 1,
                "next_stake": self.initial_stake,
                "cycle_completed": False
            }

if __name__ == "__main__":
    cm = CompoundManager()
    print("Simulación de Ciclo Soros 4 Niveles al 85% de Payout:")
    for i in range(1, 5):
        stake = cm.get_current_stake()
        res = cm.register_result(is_win=True)
        print(f"  Op {i}: Apostó ${stake:.2f} | Ganó ${res['profit']:.2f} | Siguiente nivel: {res['next_level']} con ${res['next_stake']:.2f}")
