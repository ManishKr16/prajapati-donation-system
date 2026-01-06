// Load logged-in user data
document.getElementById("name").innerText =
  localStorage.getItem("name");

document.getElementById("mobile").innerText =
  localStorage.getItem("mobile");

function payNow() {
  const amount = Number(document.getElementById("amount").value);

  // 🔒 Minimum amount check
  if (!amount || amount < 151) {
    alert("❌ Minimum donation amount is ₹151");
    return;
  }

  const upiId = "8862966605@ibl"; // temporary personal UPI
  const payeeName = "Prajapati Club";
  const note = "Donation 2026";

  const upiIntent =
    `upi://pay?pa=${upiId}&pn=${encodeURIComponent(payeeName)}&am=${amount}&cu=INR&tn=${encodeURIComponent(note)}`;

  // 🔥 Opens UPI app chooser
  window.location.href = upiIntent;
}
