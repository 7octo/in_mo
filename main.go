package main
func main() {
	// Parse command line
	filename := flag.String("file", "", "Script filename in MinIO")
	bucket := flag.String("bucket", "", "MinIO bucket name")
	signature := flag.String("sig", "", "SHA-256 signature")
	flag.Parse()

	if *filename == "" || *bucket == "" || *signature == "" {
		log.Fatal("Missing required arguments")
	}

	if err := downloadAndRun(*filename, *bucket, *signature); err != nil {
		log.Fatalf("Agent failed: %v", err)
	}
}
