import { useEffect, useState } from "react";
import ExpenseForm from "./components/ExpenseForm";

type Expense = {
  id: number;
  title: string;
  amount: number;
  category: string;
};

function App() {
  const [expenses, setExpenses] = useState<Expense[]>(() => {
    const stored = localStorage.getItem("expenses");
    return stored ? JSON.parse(stored) : [];
  });
  const [filter, setFilter] = useState("All");

  const addExpense = (expense: Expense) => {
    setExpenses((prev) => [...prev, expense]);
  };

  const deleteExpense = (id: number) => {
    setExpenses((prev) => prev.filter((exp) => exp.id !== id));
  };

  // SAVE TO LOCAL STORAGE
  useEffect(() => {
    localStorage.setItem("expenses", JSON.stringify(expenses));
  }, [expenses]);

  const total = expenses.reduce((sum, exp) => sum + exp.amount, 0);

  const filteredExpenses =
  filter === "All"
    ? expenses
    : expenses.filter((exp) => exp.category === filter);

return (
  <div style={{ padding: "20px", fontFamily: "Arial", maxWidth: "600px", margin: "auto" }}>
    <h1 style={{ textAlign: "center" }}>SmartExpense Tracker 💰</h1>

    <div style={{
      background: "#f4f4f4",
      padding: "15px",
      borderRadius: "10px",
      marginBottom: "20px",
      textAlign: "center"
    }}>
      <h2>Total Balance</h2>
      <h1 style={{ color: "green" }}>₹ {total}</h1>
    </div>

    <ExpenseForm addExpense={addExpense} />

    <div style={{ margin: "20px 0", textAlign: "center" }}>
  <select
    value={filter}
    onChange={(e) => setFilter(e.target.value)}
    style={{ padding: "8px" }}
  >
    <option value="All">All</option>
    <option value="Food">Food</option>
    <option value="Travel">Travel</option>
    <option value="Shopping">Shopping</option>
    <option value="Bills">Bills</option>
  </select>
</div>

    <h2>Expenses</h2>

    filteredExpenses.length === 0
      <p style={{ textAlign: "center" }}>No expenses added yet</p>
    ) : (
       filteredExpenses.map((exp) => (
        <div
          key={exp.id}
          style={{
            border: "1px solid #ddd",
            borderRadius: "10px",
            margin: "10px 0",
            padding: "10px",
            background: "#fff",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center"
          }}
        >
          <div>
            <h3 style={{ margin: 0 }}>{exp.title}</h3>
            <p style={{ margin: 0, color: "gray" }}>{exp.category}</p>
          </div>

          <div style={{ textAlign: "right" }}>
            <p style={{ margin: 0, fontWeight: "bold" }}>₹ {exp.amount}</p>
            <button
              onClick={() => deleteExpense(exp.id)}
              style={{
                marginTop: "5px",
                background: "red",
                color: "white",
                border: "none",
                padding: "5px 10px",
                borderRadius: "5px",
                cursor: "pointer"
              }}
            >
              Delete
            </button>
          </div>
        </div>
      ))
    )}
  </div>
);
 
