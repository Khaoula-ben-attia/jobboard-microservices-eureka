/*package com.awd.candidat.controller;

import com.awd.candidat.client.JobDto;
import feign.FeignException;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;import org.springframework.web.server.ResponseStatusException;

import java.util.List;

public class CandidateJobController {
    @GetMapping("/open-jobs")
    @Operation(summary = "List open jobs, optionally by category")
    public List<JobDto> openJobs(@RequestParam(required = false) Long categoryId) {
        try {
            return candidateJobService.openJobs(categoryId);
        } catch (FeignException.NotFound e) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Category not found");
        } catch (FeignException e) {
            throw new ResponseStatusException(HttpStatus.SERVICE_UNAVAILABLE, "Job service unavailable");
        }

    }




}
*/

