function ExpenseList({ expenses, deleteExpense }) {
  return (
    <div>
      <h2>Expenses</h2>

      {expenses.length === 0 ? (
        <p>No expenses added yet</p>
      ) : (
        expenses.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid gray",
              padding: "10px",
              marginBottom: "10px",
            }}
          >
            <h3>{item.title}</h3>
            <p>₹ {item.amount}</p>
            <p>{item.category}</p>
            <p>{item.date}</p>

            <button onClick={() => deleteExpense(item.id)}>
              Delete
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ExpenseList; 