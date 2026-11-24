package com.awd.candidat.client;

import java.time.LocalDate;

public record JobDto(Long id, String name, String description,
                     boolean available, LocalDate date, CategoryDto category) {
}
