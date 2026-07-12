import React, { useState } from "react";

interface Expense {
  id: string;
  title: string;
  amount: number;
  category: string;
  date: string;
}

export default function App() {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("Food");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !amount) return;

    const newExpense: Expense = {
      id: crypto.randomUUID(),
      title,
      amount: parseFloat(amount),
      category,
      date: new Date().toLocaleDateString(),
    };

    setExpenses([newExpense, ...expenses]);
    setTitle("");
    setAmount("");
  };

  return (
    <div style={{ maxWidth: "500px", margin: "50px auto", padding: "20px", fontFamily: "sans-serif" }}>
      <h1 style={{ textAlign: "center" }}>SmartExpense Tracker</h1>
      
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "10px", marginBottom: "30px" }}>
        <input
          type="text"
          placeholder="Expense Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
        />
        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
        >
          <option value="Food">Food</option>
          <option value="Transport">Transport</option>
          <option value="Entertainment">Entertainment</option>
          <option value="Utilities">Utilities</option>
        </select>
        <button type="submit" style={{ padding: "10px", backgroundColor: "#0070f3", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}>
          Add Expense
        </button>
      </form>

      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        {expenses.length === 0 ? (
          <p style={{ textAlign: "center", color: "#666" }}>No expenses added yet</p>
        ) : (
          expenses.map((exp) => (
            <div
              key={exp.id}
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                padding: "15px",
                border: "1px solid #eee",
                borderRadius: "5px",
                backgroundColor: "#fafafa"
              }}
            >
              <div style={{ flex: 1 }}>
                <strong style={{ display: "block" }}>{exp.title}</strong>
                <small style={{ color: "#888" }}>{exp.category} • {exp.date}</small>
              </div>
              <span style={{ fontWeight: "bold", color: "#d32f2f" }}>-${exp.amount.toFixed(2)}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}


 
