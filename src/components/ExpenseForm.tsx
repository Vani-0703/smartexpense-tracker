import { useState } from "react";

type Expense = {
  id: number;
  title: string;
  amount: number;
  category: string;
};

type Props = {
  addExpense: (expense: Expense) => void;
};

function ExpenseForm({ addExpense }: Props) {
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!title || !amount || !category) return;

    const newExpense: Expense = {
      id: Date.now(),
      title,
      amount: Number(amount),
      category,
    };

    addExpense(newExpense);

    setTitle("");
    setAmount("");
    setCategory("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: "20px" }}>
      <h2>Add Expense</h2>

      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Amount"
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />

      <br /><br />

      <select value={category} onChange={(e) => setCategory(e.target.value)}>
        <option value="">Select Category</option>
        <option value="Food">Food</option>
        <option value="Travel">Travel</option>
        <option value="Shopping">Shopping</option>
        <option value="Bills">Bills</option>
      </select>

      <br /><br />

      <button type="submit">Add Expense</button>
    </form>
  );
}

export default ExpenseForm;