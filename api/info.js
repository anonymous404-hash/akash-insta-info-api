export default async function handler(req, res) {
  const { username } = req.query;

  // External API (original)
  const apiUrl = `https://isal.isalhackerdeveloper.workers.dev/info?username=${username}`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();

    // Custom response with your name
    res.status(200).json({
      status: true,
      developer: "AKASHHACKER",
      powered_by: "AKASHHACKER",
      data: data
    });

  } catch (err) {
    res.status(500).json({
      status: false,
      developer: "AKASHHACKER",
      error: "API Fetch Failed"
    });
  }
}
