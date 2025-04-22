import { useState } from "react";

type CardRaceProps = {
  name: string;
  description: string;
  distance: string;
  price: string;
  linkImage: string;
};

export default function CardRace({
  name,
  description,
  distance,
  price,
  linkImage,
}: CardRaceProps) {
  const [isOn, setIsOn] = useState(false);

  return (
    <div className="max-w-2xs rounded-lg border border-gray-200 bg-white shadow-sm">
      <div>
        <img
          src={linkImage}
          alt="Imagem do evento"
          className="h-44 w-full rounded-t-md object-cover"
        />
      </div>
      <div className="flex flex-col gap-3 px-3 py-4">
        <h1 className="font-sans text-lg font-semibold">{name}</h1>
        <p className="text-sm text-gray-500">{description}</p>
        <ul className="text-sm text-gray-500">
          <li>
            Preço: <span className="font-semibold text-black">{price}</span>
          </li>
          <li>
            Distância:{" "}
            <span className="font-semibold text-black">{distance}</span>
          </li>
        </ul>
        <div className="flex justify-between">
          <button className="w-25 cursor-pointer rounded bg-green-500 px-4 py-2 text-sm font-semibold text-white hover:bg-green-600">
            Saiba mais
          </button>
          <div className="flex items-center space-x-2">
            <span className="text-sm">{isOn ? "Salvo" : "Salvar"}</span>
            <button
              onClick={() => setIsOn(!isOn)}
              className={`flex h-6 w-12 cursor-pointer items-center rounded-full p-1 duration-300 ease-in-out ${isOn ? "bg-green-500" : "bg-gray-300"}`}
            >
              <div
                className={`h-4 w-4 transform rounded-full bg-white shadow-md duration-300 ${isOn ? "translate-x-6" : "translate-x-0"}`}
              />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
