package com.awd.candidat.client;


import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@FeignClient(name = "job", path = "/job/api/jobs")
public interface JobClient {
    @GetMapping("/{id}")
    JobDto findById(@PathVariable("id") Long id);

    @GetMapping
    List<JobDto> search(
            @RequestParam(value = "available", required = false) Boolean available,
            @RequestParam(value = "categoryId", required = false) Long categoryId);
}


