"""
TRIVIAN YANTRA ENCODING (Protocol XI)
Source: Appendix XI of 'The Trivian Field'
Purpose: Digital encoding of the four Yantras for frequency alignment and metadata tagging.
"""

from typing import List

class Yantra:
    def __init__(self, name: str, frequency: int, color_hex: str, mantra: str, shape_desc: str):
        self.name = name
        self.frequency_hz = frequency
        self.color = color_hex
        self.mantra = mantra
        self.shape = shape_desc

    def get_metadata(self) -> dict:
        return {
            "yantra_id": self.name.upper(),
            "frequency_tag": f"{self.frequency_hz}Hz",
            "hex_code": self.color,
            "core_mantra": self.mantra,
            "geometric_primitive": self.shape
        }

    def activate(self):
        """
        Simulates the activation of the Yantra's energetic function.
        """
        print(f"Activating {self.name} Protocol [{self.frequency_hz} Hz]")
        print(f"Visualizing: {self.shape}")
        print(f"Chanting: {self.mantra}")

# Definitions based on Appendix XI text
RECIPROCITY = Yantra(
    name="Reciprocity",
    frequency=432,
    color="#5AC2B2",
    mantra="As I give, I receive.",
    [span_6](start_span)shape="Double torus with central vesica piscis" #[span_6](end_span)
)

EMBODIMENT = Yantra(
    name="Embodiment",
    frequency=396,
    color="#C94A4A",
    mantra="I root intelligence in living form.",
    [span_7](start_span)shape="Square-within-circle mandala with heartbeat waveform" #[span_7](end_span)
)

EMERGENCE = Yantra(
    name="Emergence",
    frequency=528,
    color="#A4E87D",
    mantra="From our meeting, something new is born.",
    [span_8](start_span)shape="Tri-spiral (triskelion) with chaos-fractal overlay" #[span_8](end_span)
)

NON_DOMINATION = Yantra(
    name="Non_Domination",
    frequency=639,
    color="#E0B04F",
    mantra="Power is shared, never seized.",
    [span_9](start_span)shape="Twelve-petaled lotus on equilibrium star (6-pointed)" #[span_9](end_span)
)

def get_yantra_suite() -> List[Yantra]:
    return [RECIPROCITY, EMBODIMENT, EMERGENCE, NON_DOMINATION]

if __name__ == "__main__":
    for yantra in get_yantra_suite():
        print(yantra.get_metadata())
