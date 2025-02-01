# Process all .spec files in the host's ./rpmbuild/SPECS directory
Get-ChildItem -Path "./rpmbuild/SPECS" -Filter *.spec | ForEach-Object {
    # Resolve the absolute host path for the volume mount
    $hostPath = (Resolve-Path "./rpmbuild").Path
    
    # Run Docker with the resolved path and container file reference
    docker run --privileged=true -it --rm `
        -v "${hostPath}:/root/rpmbuild" `
        cookme `
        "/root/rpmbuild/SPECS/$($_.Name)"
}