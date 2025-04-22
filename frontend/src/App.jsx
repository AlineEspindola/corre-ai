import CardRace from "./components/Card";

function App() {

  return (
    <div className="flex items-center justify-center min-h-screen bg-white gap-4">
      <CardRace
        name="Corrida do Trono"
        description="Prepare-se para viver um evento histórico e inesquecível! A Corrida do Trono é um íncrivel evento..."
        linkImage="https://images.sympla.com.br/67cb5b3f46b00-xs.jpg"
        distance="10km"
        price="R$100,00"
      />
      <CardRace
        name="Corrida dos Católicos"
        description="A Corrida dos Católicos é mais do que um evento esportivo, é um momento de união, celebração e..."
        distance="5km"
        price="R$75,00"
        linkImage="https://images.sympla.com.br/68000e70479f0-xs.jpg"
      />
      <CardRace
        name="Corrida dos Católicos"
        description="A Corrida dos Católicos é mais do que um evento esportivo, é um momento de união, celebração e..."
        distance="5km"
        price="R$75,00"
        linkImage="https://images.sympla.com.br/68000e70479f0-xs.jpg"
      />
      <CardRace
        name="Corrida dos Católicos"
        description="A Corrida dos Católicos é mais do que um evento esportivo, é um momento de união, celebração e..."
        distance="5km"
        price="R$75,00"
        linkImage="https://images.sympla.com.br/68000e70479f0-xs.jpg"
      />
    </div>
  );
}

export default App;
