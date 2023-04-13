import { useState } from "react";

export default function HideableElement({text} : {text : string}) {
  const [visible, setVisible] = useState(false);

  return (
    <div>
      <button onClick={() => setVisible(!visible)}>
        {visible ? 'Cacher' : 'Afficher'}
      </button>
      {visible && <p>{text}</p>}
    </div>
  );
}