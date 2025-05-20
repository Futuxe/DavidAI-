import React from "react";

const Sidebar = ({ history }) => {
  return (
    <aside>
      <h2>Historia</h2>
      <ul>
        {history.map((item, idx) => (
          <li key={idx}>
            <strong>{item.prompt}</strong>
            <pre>
              <code>{item.code}</code>
            </pre>
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default Sidebar;
