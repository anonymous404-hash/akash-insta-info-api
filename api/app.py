export default async function handler(req, res) {
  const { username } = req.query;
  const targetUser = username || "1sortex";
  const apiUrl = `https://isal.isalhackerdeveloper.workers.dev/info?username=${targetUser}`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();

    // Aapka Branding add kar diya
    const customResponse = {
      ...data,
      "developer": "AKASHHACKER",
      "status": "Success"
    };

    res.status(200).json(customResponse);
  } catch (error) {
    res.status(500).json({ error: "API Down", developer: "AKASHHACKER" });
  }
}
